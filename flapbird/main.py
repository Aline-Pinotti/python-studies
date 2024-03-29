import pygame # biblioteca mais utilizada para criação de jogos
import os     # para acessar os caminhos do sistema (e trazer as imagens dos jogos)
import random

SH = 800
SW = 500

IMG_PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMG_BASE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMG_BKG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMGS_BRD = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png'))),
]

pygame.font.init()
FONT_SCORE = pygame.font.SysFont('arial', 50)

class Passaro:
    IMGS = IMGS_BRD
    # animações da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.speed = 0
        self.height = self.y
        self.time = 0
        self.img_count = 0
        self.img = self.IMGS[0]
        
    def pular(self):
        self.speed = -10.5
        self.time = 0
        self.height = self.y
    
    def mover(self):
        #calcular o deslocamento
        self.time += 1 # a cada milésimo de segundo/frame
        #Fórmula da asceleração ("sorvetão") S = so + vot + at^2/2
        deslocamento = 1.5 * (self.time**2) + self.speed * self.time
        
        #restringir o deslocamento (garantir que não vão acontecer coisas absurdas)
        if deslocamento > 16: #deslocamento máximo 16
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2 # ganho extra quando pula para jogabilidade - pode fazer sem isso
        
        self.y += deslocamento
        
        #ângulo do pássaro (para animação)
        if deslocamento < 0 or self.y < (self.height + 50): # se o pássaro está se deslocando para cima - o or pra frente é pro pássaro não virar pra baixo logo no topo
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO
        
    def desenhar(self, tela):
        # definir quel imagem do pássaro vai usar
        self.img_count += 1
        
        if self.img_count < self.TEMPO_ANIMACAO:
            self.img = self.IMGS[0]
        elif self.img_count < self.TEMPO_ANIMACAO*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.TEMPO_ANIMACAO*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.TEMPO_ANIMACAO*4:
            self.img = self.IMGS[1]
        elif self.img_count >= self.TEMPO_ANIMACAO*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0        
            
        # se o pássaro tiver caindo eu não vou bater asa
        if self.angulo <= -80: # ajuste "fino"
            self.img = self.IMGS[1]
            self.img_count = self.TEMPO_ANIMACAO*2
        
        # desenhar imagem
        img_rot = pygame.transform.rotate(self.img, self.angulo)
        pos_centro_img = self.img.get_rect(topleft=(self.x, self.y)).center
        rect = img_rot.get_rect(center=pos_centro_img) #definindo um perímetro para a imagem
        tela.blit(img_rot, rect.topleft)
        
    def get_mask(self): # pega a máscara do pássaro (que identifica, dentro do quadrado/perímetro definido pro pássaro, onde tem a imagem do pássaro - pixel por pixel)
        return pygame.mask.from_surface(self.img)

class Cano:
    DIST = 200
    SPEED = 5
    
    def __init__(self, x):
        self.x = x
        self.h = 0
        self.pos_top = 0
        self.pos_base = 0
        self.PIPE_TOPO = pygame.transform.flip(IMG_PIPE, False, True) # imagem, flipa na horizontal, flipa na vertical
        self.PIPE_BASE = IMG_PIPE
        self.passou = False
        self.definir_altura()
        
    def definir_altura(self):
        self.h = random.randrange(50, 450)
        self.pos_top = self.h - self.PIPE_TOPO.get_height()
        self.pos_base = self.h + self.DIST
        
    def mover(self):
        self.x -= self.SPEED
        
    def desenhar(self, tela):
        tela.blit(self.PIPE_TOPO, (self.x, self.pos_top))
        tela.blit(self.PIPE_BASE, (self.x, self.pos_base))
        
    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.PIPE_TOPO)
        base_mask = pygame.mask.from_surface(self.PIPE_BASE)
        
        dist_topo = (self.x - passaro.x, self.pos_top - round(passaro.y))
        dist_base = (self.x - passaro.x, self.pos_base - round(passaro.y))
        
        topo_ponto = passaro_mask.overlap(topo_mask, dist_topo)
        base_ponto = passaro_mask.overlap(base_mask, dist_base)
        
        if topo_ponto or base_ponto:
            return True
        else:
            return False

class Chao:
    SPEED = 5
    WID = IMG_BASE.get_width() #LARGURA
    IMG = IMG_BASE
    
    def __init__(self, y):
        self.y = y
        self.x0 = 0
        self.x1 = self.WID
        
    def mover(self):
        self.x0 -= self.SPEED
        self.x1 -= self.SPEED
        
        if self.x0 + self.WID < 0:
            self.x0 = self.x1 + self.WID
        
        if self.x1 + self.WID < 0:
            self.x1 = self.x0 + self.WID
            
    def desenhar(self, tela):
        tela.blit(self.IMG, (self.x0, self.y))
        tela.blit(self.IMG, (self.x1, self.y))
        
def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMG_BKG, (0, 0))
    
    for p in passaros: #para futura implementação de inteligência artificial, treinar vários pássaros
        p.desenhar(tela)
    
    for c in canos:
        c.desenhar(tela)
        
    texto = FONT_SCORE.render(f'Pontuação: {pontos}', 1, (255, 255, 255))
    tela.blit(texto, (SW - 10 - texto.get_width(), 10))
    chao.desenhar(tela)
    pygame.display.update()
    
def main():
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((SW, SH))
    pontos = 0
    relogio = pygame.time.Clock()
    
    #while True: # um jogo é um loop infinito
    
    rodando = True
    while rodando:
        relogio.tick(30)
        
        # interação como usuário
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    for passaro in passaros:
                        passaro.pular()
        
        # mover as coisas                
        for passaro in passaros:
            passaro.mover()
            
        chao.mover()
                
        adc_cano = False
        remover_canos = [] # para nao remover dentro do for
        
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    passaros.pop(i)
                if not cano.passou and passaro.x > cano.x:
                    adc_cano = True
            cano.mover()
            if cano.x + cano.PIPE_TOPO.get_width() < 0: #quer dizer q o cano saiu da tela
                remover_canos.append(cano)
        
        if adc_cano:
            pontos += 1
            canos.append(Cano(600))
        
        for cano in remover_canos:
            canos.remove(cano)
            
        #tratar a colisão do pássaro com chão ou teto
        
        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.img.get_height()) > chao.y or passaro.y < 0:
                passaros.pop(i)
        
        if len(passaros) == 0: #se o passarinho morre, tem q parar o jogo e mostrar a pontuação, ou um "GAME OVER"
            break
            
        
        desenhar_tela(tela, passaros, canos, chao, pontos)
    
if __name__ == '__main__':
    main()