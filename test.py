import random
clans_dictionary_with_answers = {"Raitoningu": {"firstquestion": 1,
                                                "name":"Raitoningu",
                                                "secondquestion": 1,
                                                "thirdquestion": 1,
                                                "fourthquestion": 1},
                                 "Same": {"firstquestion": 1,
                                                "name": "Same",
                                                "secondquestion": 1,
                                                "thirdquestion": 2,
                                                "fourthquestion": 1},
                                 "Chimamire no kiri": {"firstquestion": 1,
                                                "name": "Chimamire no kiri",
                                                "secondquestion": 1,
                                                "thirdquestion": 1,
                                                "fourthquestion": 2},
                                 "Mizunoken": {"firstquestion": 1,
                                                "name": "Mizunoken",
                                                "secondquestion": 1,
                                                "thirdquestion": 2,
                                                "fourthquestion": 2},
                                 "Tekondō": {"firstquestion": 1,
                                                "name": "Tekondō",
                                                "secondquestion": 2,
                                                "thirdquestion": 1,
                                                "fourthquestion": 1},
                                 "Jakkaru": {"firstquestion": 1,
                                                "name": "Jakkaru",
                                                "secondquestion": 2,
                                                "thirdquestion": 2,
                                                "fourthquestion": 1},
                                 "Kin'iro no me": {"firstquestion": 1,
                                                "name": "Kin'iro no me",
                                                "secondquestion": 2,
                                                "thirdquestion": 1,
                                                "fourthquestion": 2},
                                 "Doku": {"firstquestion": 1,
                                                "name": "Doku",
                                                "secondquestion": 2,
                                                "thirdquestion": 2,
                                                "fourthquestion": 2},
                                 "Shibō": {"firstquestion": 2,
                                                "name": "Shibō",
                                                "secondquestion": 1,
                                                "thirdquestion": 1,
                                                "fourthquestion": 1},
                                 "Chikaku-teki": {"firstquestion": 2,
                                                "name": "Chikaku-teki",
                                                "secondquestion": 1,
                                                "thirdquestion": 2,
                                                "fourthquestion": 1},
                                 "Atsuryoku-ten": {"firstquestion": 2,
                                                "name": "Atsuryoku-ten",
                                                "secondquestion": 1,
                                                "thirdquestion": 1,
                                                "fourthquestion": 2},
                                 "Inu no tomodachi": {"firstquestion": 2,
                                                "name": "Inu no tomodachi",
                                                "secondquestion": 1,
                                                "thirdquestion": 2,
                                                "fourthquestion": 2},
                                 "Hakushoku hikari": {"firstquestion": 2,
                                                "name": "Hakushoku hikari",
                                                "secondquestion": 2,
                                                "thirdquestion": 1,
                                                "fourthquestion": 1},
                                 "Wāmu": {"firstquestion": 2,
                                                "name": "Wāmu",
                                                "secondquestion": 2,
                                                "thirdquestion": 2,
                                                "fourthquestion": 1},
                                 "Hen'i-tai": {"firstquestion": 2,
                                                "name": "Hen'i-tai",
                                                "secondquestion": 2,
                                                "thirdquestion": 2,
                                                "fourthquestion": 2},
                                 "Shinkō": {"firstquestion": 2,
                                                "name": "Shinkō",
                                                "secondquestion": 2,
                                                "thirdquestion": 1,
                                                "fourthquestion": 2},
                                 "Ningyō": {"firstquestion": 3,
                                                "name": "Ningyō",
                                                "secondquestion": 1,
                                                "thirdquestion": 1,
                                                "fourthquestion": 1},
                                 "Kusuri": {"firstquestion": 3,
                                                "name": "Kusuri",
                                                "secondquestion": 1,
                                                "thirdquestion": 2,
                                                "fourthquestion": 1},
                                 "Shadouasashin": {"firstquestion": 3,
                                                "name": "Shadouasashin",
                                                "secondquestion": 1,
                                                "thirdquestion": 1,
                                                "fourthquestion": 2},
                                 "Kōri": {"firstquestion": 3,
                                                "name": "Kōri",
                                                "secondquestion": 1,
                                                "thirdquestion": 2,
                                                "fourthquestion": 2},
                                 "Ketsueki": {"firstquestion": 3,
                                                "name": "Ketsueki",
                                                "secondquestion": 2,
                                                "thirdquestion": 1,
                                                "fourthquestion": 1},
                                 "Shinrin": {"firstquestion": 3,
                                                "name": "Shinrin",
                                                "secondquestion": 2,
                                                "thirdquestion": 2,
                                                "fourthquestion": 1},
                                 "Hagane": {"firstquestion": 3,
                                                "name": "Hagane",
                                                "secondquestion": 2,
                                                "thirdquestion": 1,
                                                "fourthquestion": 2},
                                 "Maguneshiumu": {"firstquestion": 3,
                                                "name": "Raitoningu",
                                                "secondquestion": 2,
                                                "thirdquestion": 2,
                                                "fourthquestion": 2},
                                 "Kopī": {"firstquestion": 4,
                                                "name": "Kopī",
                                                "secondquestion": 1,
                                                "thirdquestion": 1,
                                                "fourthquestion": 1},
                                 "Kage no senshi": {"firstquestion": 4,
                                                "name": "Kage no senshi",
                                                "secondquestion": 1,
                                                "thirdquestion": 2,
                                                "fourthquestion": 1},
                                 "Mippei suru": {"firstquestion": 4,
                                                "name": "Mippei suru",
                                                "secondquestion": 1,
                                                "thirdquestion": 1,
                                                "fourthquestion": 2},
                                 "Maindo": {"firstquestion": 4,
                                                "name": "Maindo",
                                                "secondquestion": 1,
                                                "thirdquestion": 2,
                                                "fourthquestion": 2},
                                 "Arashi": {"firstquestion": 4,
                                                "name": "Arashi",
                                                "secondquestion": 2,
                                                "thirdquestion": 1,
                                                "fourthquestion": 1},
                                 "Taimatsu": {"firstquestion": 4,
                                                "name": "Taimatsu",
                                                "secondquestion": 2,
                                                "thirdquestion": 2,
                                                "fourthquestion": 1},
                                 "Shizen": {"firstquestion": 4,
                                                "name": "Shizen",
                                                "secondquestion": 2,
                                                "thirdquestion": 1,
                                                "fourthquestion": 2},
                                 "Kemuri": {"firstquestion": 4,
                                                "name": "Kemuri",
                                                "secondquestion": 2,
                                                "thirdquestion": 2,
                                                "fourthquestion": 2},
                                 "Hikari": {"firstquestion": 4,
                                                "name": "Hikari",
                                                "secondquestion": 2,
                                                "thirdquestion": 1,
                                                "fourthquestion": 1},
                                 "Kumo": {"firstquestion": 4,
                                                "name": "Kumo",
                                                "secondquestion": 2,
                                                "thirdquestion": 2,
                                                "fourthquestion": 2},
                                }

clans_list = ['Raitoningu',"Same","Chimamire no kiri","Mizunoken","Tekondō","Jakkaru","Kin'iro no me","Doku","Shibō","Chikaku-teki","Atsuryoku-ten","Inu no tomodachi","Wāmu","Hakushoku hikari","Hen'i-tai","Shinkō","Ningyō","Kusuri","Shadouasashin","Kōri","Ketsueki","Shinrin","Hagane","Maguneshiumu","Kopī","Kage no senshi","Mippei suru","Maindo","Arashi","Taimatsu","Shizen","Kemuri","Hikari","Kumo"]
clans_list_after_first_question = []
clans_list_after_second_question = []
clans_list_after_third_question = []
clans_list_after_fourth_question = []


def character_clan_answers_logic(first_question_answer,second_question_answer,third_question_answer,fourth_question_answer):
    character_clan_answers_logic_checker = 0
    first_question = first_question_answer
    second_question = second_question_answer
    third_question = third_question_answer
    fourth_question = fourth_question_answer
    if first_question == '1':
        for i in range(len(clans_list)):
            if clans_dictionary_with_answers[clans_list[i]]["firstquestion"] == 1:
                clans_list_after_first_question.append(clans_dictionary_with_answers[clans_list[i]]["name"])
    if first_question == "2":
        for i in range(len(clans_list)):
            if clans_dictionary_with_answers[clans_list[i]]["firstquestion"] == 2:
                clans_list_after_first_question.append(clans_dictionary_with_answers[clans_list[i]]["name"])
    if first_question == '3':
        for i in range(len(clans_list)):
            if clans_dictionary_with_answers[clans_list[i]]["firstquestion"] == 3:
                clans_list_after_first_question.append(clans_dictionary_with_answers[clans_list[i]]["name"])
    if first_question == "4":
        for i in range(len(clans_list)):
            if clans_dictionary_with_answers[clans_list[i]]["firstquestion"] == 4:
                clans_list_after_first_question.append(clans_dictionary_with_answers[clans_list[i]]["name"])
    if second_question == '1':
        for i in range(len(clans_list_after_first_question)):
            if clans_dictionary_with_answers[clans_list_after_first_question[i]]["secondquestion"] == 1:
                clans_list_after_second_question.append(clans_dictionary_with_answers[clans_list_after_first_question[i]]["name"])
    if second_question == "2":
        for i in range(len(clans_list_after_first_question)):
            if clans_dictionary_with_answers[clans_list_after_first_question[i]]["secondquestion"] == 2:
                clans_list_after_second_question.append(clans_dictionary_with_answers[clans_list_after_first_question[i]]["name"])
    if third_question == "1":
        for i in range(len(clans_list_after_second_question)):
            if clans_dictionary_with_answers[clans_list_after_second_question[i]]["thirdquestion"] == 1:
                clans_list_after_third_question.append(clans_dictionary_with_answers[clans_list_after_second_question[i]]["name"])
    if third_question == '2':
        for i in range(len(clans_list_after_second_question)):
            if clans_dictionary_with_answers[clans_list_after_second_question[i]]["thirdquestion"] == 2:
                clans_list_after_third_question.append(clans_dictionary_with_answers[clans_list_after_second_question[i]]["name"])
    if fourth_question == "1":
        for i in range(len(clans_list_after_third_question)):
            if clans_dictionary_with_answers[clans_list_after_third_question[i]]["fourthquestion"] == 1:
                clans_list_after_fourth_question.append(clans_dictionary_with_answers[clans_list_after_second_question[i]]["name"])
                character_clan_answers_logic_checker =1
    if fourth_question == "2":
        for i in range(len(clans_list_after_third_question)):
            if clans_dictionary_with_answers[clans_list_after_third_question[i]]["fourthquestion"] == 2:
                clans_list_after_fourth_question.append(clans_dictionary_with_answers[clans_list_after_second_question[i]]["name"])
                character_clan_answers_logic_checker =1
    #final_first_clan = random.choice(clans_list_after_fourth_question)
    #print("your class is: " + final_first_clan)
    if character_clan_answers_logic_checker == 1:
        final_first_clan = random.choice(clans_list_after_fourth_question)
        print("your class is: " + final_first_clan)

character_clan_answers_logic("3","2","2","2")