nounlist =[[101,0.59,0.75,2.03,69.5,"Бесарабський"],
        [101,0.74,0.83,2.08,70,"Сінний"],
        [101,0.7,0.83,2.04,40,"Лук'янівський"],
        [102,0.38,0.65,2.4,45,"Бесарабський"],
        [102,0.36,0.6,2.3,44.6,"Лук'янівський"],
        [102,0.59,0.75,2.03,69.5,"Сінний"],
        [103,0.63,0.79,2.04,40,"Бесарабський"],
        [103,0.63,0.75,2,68,"Лук'янівський"],
        [103,0.36,0.6,2.35,44.8,"Сінний"],
        [201,0.69,0.99,4.52,30,"Бесарабський"],
        [201,0.68,0.98,4.5,29.6,"Лук'янівський"],
        [201,0.69,0.95,4.45,29.6,"Сінний"],
        [202,0.88,1.24,4.56,25,"Бесарабський"],
        [202,0.87,1.22,4.53,25,"Лук'янівський"],
        [202,0.85,1.24,4.55,25,"Сінний"],
        [203,1.1,33,5.77,70,"Бесарабський"],
        [203,0.99,1.31,5.75,68.9,"Лук'янівський"],
        [203,0.99,1.33,5.75,69,"Сінний"],]

print(": Товар  :Ціна 2007   :Ціна 2008   :Ціна 2011   :Ціна 2017   :Ринок")

for item in nounlist:
    print(":",item[0]," "*(5-len(str(item[0]))),":",
    item[1]," "*(9-len(str(item[1]))),":",
    item[2]," "*(9-len(str(item[2]))),":",
    item[3]," "*(9-len(str(item[3]))),":",
    item[4]," "*(9-len(str(item[4]))),":",
    item[5]," "*(-len(item[5]))),":"