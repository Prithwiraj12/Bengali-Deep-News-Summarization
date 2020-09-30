from rouge import FilesRouge
ref_path = "/home/avivilla/Desktop/MLproject/AbstractBengali/ref.txt"
hyp_path = "/home/avivilla/Desktop/MLproject/AbstractBengali/hyp.txt"
files_rouge = FilesRouge()
avg_scores = files_rouge.get_scores(hyp_path, ref_path,avg=True)
scores = files_rouge.get_scores(hyp_path, ref_path)
with open("/home/avivilla/Desktop/MLproject/AbstractBengali/bleuROugeAnalysis.txt",'w') as outputfile :
    outputfile.write("Average Rouge Score : \n")
    outputfile.write("ROUGE-1 ----  ")
    rouge =  avg_scores['rouge-1']
    outputfile.write("f1-score : ")
    outputfile.write("{:2.4f}".format(rouge['f']))
    outputfile.write("  recall : ")
    outputfile.write("{:2.4f}".format(rouge['r']))
    outputfile.write("  precision : ")
    outputfile.write("{:2.4f}".format(rouge['p']))
    outputfile.write("\n")

    outputfile.write("ROUGE-2 ----  ")
    rouge =  avg_scores['rouge-2']
    outputfile.write("f1-score : ")
    outputfile.write("{:2.4f}".format(rouge['f']))
    outputfile.write("  recall : ")
    outputfile.write("{:2.4f}".format(rouge['r']))
    outputfile.write("  precision : ")
    outputfile.write("{:2.4f}".format(rouge['p']))
    outputfile.write("\n")

    outputfile.write("ROUGE-L ----  ")
    rouge =  avg_scores['rouge-l']
    outputfile.write("f1-score : ")
    outputfile.write("{:2.4f}".format(rouge['f']))
    outputfile.write("  recall : ")
    outputfile.write("{:2.4f}".format(rouge['r']))
    outputfile.write("  precision : ")
    outputfile.write("{:2.4f}".format(rouge['p']))
    outputfile.write("\n")
    outputfile.write("\n")
    outputfile.write("\n")
    outputfile.write("------------------------------------------------------------------------------------------------------------------------")
    outputfile.write("\n")
    id = 0
    for score in scores :
        id+=1
        outputfile.write("\n")
        outputfile.write("Rouge Score for Line ")
        outputfile.write(str(id))
        outputfile.write("\n")
        outputfile.write("ROUGE-1 ----  ")
        rouge =  score['rouge-1']
        outputfile.write("f1-score : ")
        outputfile.write("{:2.4f}".format(rouge['f']))
        outputfile.write("  recall : ")
        outputfile.write("{:2.4f}".format(rouge['r']))
        outputfile.write("  precision : ")
        outputfile.write("{:2.4f}".format(rouge['p']))
        outputfile.write("\n")

        outputfile.write("ROUGE-2 ----  ")
        rouge =  score['rouge-2']
        outputfile.write("f1-score : ")
        outputfile.write("{:2.4f}".format(rouge['f']))
        outputfile.write("  recall : ")
        outputfile.write("{:2.4f}".format(rouge['r']))
        outputfile.write("  precision : ")
        outputfile.write("{:2.4f}".format(rouge['p']))
        outputfile.write("\n")

        outputfile.write("ROUGE-L ----  ")
        rouge =  score['rouge-l']
        outputfile.write("f1-score : ")
        outputfile.write("{:2.4f}".format(rouge['f']))
        outputfile.write("  recall : ")
        outputfile.write("{:2.4f}".format(rouge['r']))
        outputfile.write("  precision : ")
        outputfile.write("{:2.4f}".format(rouge['p']))
        outputfile.write("\n")

        outputfile.write("\n")
        outputfile.write("------------------------------------------------------------------------------------------------------------------------")

    outputfile.close()

