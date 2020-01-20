# Introdução à Matemática e Física Para Videojogos I - Final Project - Parte 2

![fpsforms](https://temptempo.yolasite.com/resources/form%20-%20tf%20matematica%202.png)

---

## Trabalho Realizado

Para esta segunda parte do projecto, foram criadas algumas formas com preenchimento, foram implementas teclas de modo a
conseguir movimentar a câmera, foi implementado o controlo da câmera com o rato e também o *rendering* apenas de formas visíveis.

### Contribuições
### Pedro Marques - (por ordem de trabalho realizado)
#### *sample.py*
Comecei por criar algumas teclas com o valor *False* por definição. À semelhança da parte 1 do projecto criei as teclas que 
,ao serem premidas, vão incrementar a posição da câmera (*scene.camera.position*).

#### *mesh.py*
Após isto, aproveitei código da parte 1 para criar pirâmides e código original para criar cubos. Posteriormente, ainda na classe *Mesh*, no método *render* criei a forma preenchida, juntamente com o seu *wireframe*.

#### *sample.py*
Depois dos passos anteriores, coloquei o rato "preso" à janela e usei a posição do mesmo de modo a alterar os valores 
do *axis* e modificar a rotação da câmera.

Criei métodos adicionais no *object3d.py* de modo a ter acesso a todos os vetores à volta de um objecto. Acabei por usar estes métodos para a movimentação da câmera. Criei também um método *remove_object()* na *scene.py*.

Após isto, utilizei uma lista (*objList*) em que foram adicionados os objectos criados, de modo a escolher quais deles são adicionados à lista de objectos que vão ser *renderizados* (*scene.objects*). Para escolher quais são adicionados, utilizo a normal do objecto (para todos os objectos com um *for*) e retiro a posição da câmera, de modo a que a normal esteja sempre virada para o lado contrário da mesma. De seguida, faço o produto interno entre essa mesma normal e o vector da câmera. Caso o produto interno seja maior que 0, o objecto é renderizado. Para esta fase do trabalho contei com a ajuda do colega Marco Domingos.

Tendo este último passo realizado, avancei para o *Implement filled geometry*. Aproveitei o *for* criado no passo anterior para calcular a distância entre todos os objectos, fazendo com que os objectos com menor distância sejam adicionandos no fim da lista *scene.objects*. Assim, sendo que são adicioados apenas no fim, o *rendering* dos mesmos vai ser feito por cima dos objectos mais distantes.

## Dificuldades
Quanto às dificuldades que encontrei durante o desenvolvimento da parte 2, quanto ao desenvolvimento das formas não existiram dificuldades, sendo que o processo de criação foi semelhante à parte 1. Em relação ao movimento com o rato, surgiram dificuldades em perceber o porquê da rotação da câmera no eixo Z. Após estes passos tive bastantes dificuldades em perceber como aplicar o produto interno nos objectos de modo a que desaparecem por trás da câmera. No último passo, *Implement filled geometry*, apesar de não existirem dificuldades, também não consegui aplicar a teoria na perfeição, sendo que os objectos são desenhados consoante a distância apenas quando o programe é executado inicialmente.

---

## Grupo

Pedro Miguel Marques, 21900253  |  Github Account - pmarques93

Miguel Feliciano, 21904115  |  Github Account - Mike-Feliz

Luís Gomes, 21901362  |  Github Account - LuisTheGomes
