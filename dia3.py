string_escolha = "string_inicial"

print("Boas vindas aventureiro, aqui vai uma conquista de um tesouro magico, te apresento duas escolhas\n")
print("primeiro, você está em uma guilda de aventura e escuta todos falando sobre um tesouro nas ilhas Golfinhos Magicos, perto de sua casa, você escolhe partir pra sua aventura ou perguntar alguém sobre informações?\n")
string_escolha = input("Digite 'conversar' para ir atrás de outros aventureiros ou 'partir' para ja seguir em sua jornada: ")

if(string_escolha == "conversar"):
    print("Os aventureiros estão desconfiados e preferem não falar com você, poxa vida, oq você faz agora?você pode correr ou tentar arrumar um transporte")
    string_escolha = input("Digite 'correr' para correr com suas pernas ou 'montaria' para ir atrás de uma montaria: ")
    if(string_escolha == "correr"):
        print("poxa, você correu muito, porém quando chega lá você vê aventureiros ja voltando com o tesouro")
    if(string_escolha == "montaria"):
        print("você vê uma velhinha em uma carroça e vê uma professora em cima de patins na era medieval, não se questione\n")
        string_escolha = input("Digite 'velhinha' para assaltar a senhora ou 'discreta' para ir atrás dos patins: ")
        if(string_escolha == "velhinha"):
            print("QUÊ? como você tem coragem de atacar uma idosa, ela puxa um rifle de sua carroça e te transforma em uma buxa de balas, tente na proxima vida\n")
        if(string_escolha == "discreta"):
            print("Caramba, boa escolha você pegou os patins enquanto ela falava de numeros\n")
            string_escolha = input("Digite 'correr' para usar os patins ou 'comer os patins' você acha eles apetitosos: ")
            if(string_escolha == "correr"):
                print("você não sabe usar patins e acaba que os guardas te pegam, tente na proxima realidade\n")
            if(string_escolha == "comer os patins"):
                print("Estranho... porém você sente algo diferente em sua barriga, você se sente super rapido e talvez agora você possa ir com extrema velocidade pro local\n")
                string_escolha = input("digite 'comprar' para comprar um mapa ou 'ir na fé' vai que você acerta pelas suas memorias: ")
                if(string_escolha == "ir na fé"):
                    print("você acaba em uma igreja, acho que errou o caminho, agora só na proxima realidade")
                if(string_escolha == "comprar um mapa"):
                    print("você pega um mapa trocando por sua camisa e agora pode ir pro local correto que era diferente do qual você lembrava\n você vai indo super rapido e passa a maioria dos aventureiros, vrumm*\n")
                    string_escolha = input("você chega de frente pra ilha, digite 'nadar' se você se garante no braço, ou 'esperar' se você quer que alguém venha com um barco: ")
                    if(string_escolha == "esperar"):
                        print("tens alguns barcos, porém eles não querem levar pobres, puts, proxima realidade")
                    if(string_escolha == "nadar"):
                        print("UAU, você achou um tubarão amigo e ele esta te levando para a ilha em uma velocidade alta, que sorte a sua\n")
                        string_escolha = input("na ilha você vê goblins que estão dançando divertidamente, digite 'eba' para se juntar a dança divertida ou 'pera ai' se você acha que tem algo errado: ")
                        if(string_escolha == "pera ai"):
                            print("puts, você acordou e provavelmente tinha desmaiado após uma pedra cair na sua cabeça, nunca existiu tesouro")
                        if(string_escolha == "eba"):
                            print("você entrou em uma dança divertida com os goblins, eles te oferecem a goblin princesa para você se casar(você nunca a viu)")
                            string_escolha = input("digite 'casar' para aceitar se casar com ela ou 'fugir' se você só pensa no tesouro: ")
                            if(string_escolha == "fugir"):
                                print("puts, os outros goblins se sentiram desonrados, agora você virou o prato da noite, boa sorte na proxima vida")
                            if(string_escolha == "casar"):
                                print("você se casa com ela apesar de não a ter visto e descobre que era uma ogra de 3 metros e uns 500 quilos\n")
                                string_escolha = input("digite 'xixi' para fugir falando que vai fazer xixi 'pular' para pular na fogueira goblin: ")
                                if(string_escolha == "pular"):
                                    print("Você fez uma cena engraçada pulando no fogo, mas você morreu, tente na proxima realidade ou sonho...")
                                if(string_escolha == "xixi"):
                                    print("você consegue achar um caminho direto pro tesouro, também conseguiu despita-los, você vê um báu em sua frente, a jornada sera que vai ter fim?")
                                    string_escolha = input("\ndigite 'abrir' para abrir o báu ou 'amigos' se o verdadeiro tesouro foram os amigos que você fez pelo caminho: ")
                                    if(string_escolha == "abrir"):
                                        print("você acha um tesouro incrivel, porém acorda e percebe que tudo foi um sonho louco")
                                    if(string_escolha == "amigos"):
                                        print("você convenceu a princesa a se casar com seu amigo tubarão e os goblins te deram as posses de todos seus tesouros, você está rico\n")
    if(string_escolha == "partir"):
        print("eita, na real a ilha das suas lembraças era a ilha do caranguejo e não do golfinho, pelo menos você está perto de sua casa, talvez na proxima realidade\n")

