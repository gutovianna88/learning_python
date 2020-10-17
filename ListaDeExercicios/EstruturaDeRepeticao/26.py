"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""
votes = []
candidate_one = input("Digite o nome do primeiro candidato: ")
candidate_two = input("Digite o nome do segundo candidato: ")
candidate_three = input("Digite o nome do terceiro candidato: ")
vote_one = 0
vote_two = 0
vote_three = 0
white = 0
voters = int(input("Quantos eleitores irão votar? "))


while len(votes) < voters:
    print("1- ", candidate_one, "| 2- ", candidate_two, "| 3- ", candidate_three)
    vote = input("Qual seu voto? ")
    votes.append(vote)
    if vote == "1":
        vote_one = vote_one + 1
    elif vote == "2":
        vote_two = vote_two + 1
    elif vote == "3":
        vote_three = vote_three + 1
    else:
        white = white + 1


if (vote_one > vote_two and
    vote_one > vote_three and
    vote_one > white):
    print(candidate_two, vote_two)
    print(candidate_three, vote_three)
    print("Em branco ", white)
    print(candidate_one, vote_one, "Venceu ")


if (vote_two > vote_one and
    vote_two > vote_three and
    vote_two > white):
    print(candidate_one, vote_one)
    print(candidate_three, vote_three)
    print("Em branco ", white)
    print(candidate_two, vote_two, "Venceu ")


if (vote_three > vote_one and
    vote_three > vote_two and
    vote_three > white):
    print(candidate_one, vote_one)
    print(candidate_two, vote_two)
    print("Em branco ", white)
    print(candidate_three, vote_three, "Venceu ")


if (white > vote_one and
    white > vote_two and
    white > vote_three):
    print(candidate_one, vote_one)
    print(candidate_two, vote_two)
    print(candidate_three, vote_three)
    print("Em branco ", white, "Ninguem venceu! ")

