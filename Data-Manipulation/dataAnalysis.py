import re
def analyzeFile(inputFilePath,outputFilePath):
    maxFrequency = 0
    minFrequency = 100000
    cnt = 0
    distinctWords =  set([])
    lineLengthFrequency = dict([])
    totalWords = 0
    for i in range(1,100,1) :
        print(i)
        lineLengthFrequency[i] = 0
    with open(inputFilePath,'r') as inputFile:
        Lines = inputFile.readlines()
        totalLines = len(Lines)
   
        
        for line in Lines :

            cnt+=1
            words = re.split(' | ',line)

            maxFrequency = max(len(words),maxFrequency)
            minFrequency = min(len(words),minFrequency)
            lineLengthFrequency[len(words)]+=1
            totalWords+=len(words)
            for word in words:
                distinctWords.add(word)


        with open(outputFilePath,'w') as outputFile:

            outputFile.write("Total Lines : ")
            outputFile.write(str(totalLines))
            outputFile.write("\n")

            outputFile.write("Total Words : ")
            outputFile.write(str(totalWords))
            outputFile.write("\n")

            outputFile.write("Total Distinct Words : ")
            outputFile.write(str(len(distinctWords)))
            outputFile.write("\n")

            outputFile.write("Maximum Line Length : ")
            outputFile.write(str(maxFrequency))
            outputFile.write("\n")

            outputFile.write("Minimum Line Length : ")
            outputFile.write(str(minFrequency))
            outputFile.write("\n")

            outputFile.write("        Line Length Frequency : ")
            outputFile.write("\n")

            for i in range(1,100,1) :
                outputFile.write(str(i))
                outputFile.write(" : ")
                outputFile.write(str(lineLengthFrequency[i]))
                outputFile.write("\n")

            outputFile.close()

            
        
        inputFile.close()
    

analyzeFile("article.txt","articleAnalysis.txt")
analyzeFile("summary.txt","summaryAnalysis.txt")
