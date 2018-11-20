library(stringr)

#setting the parameters for the sample function
x <- c('A','C','T','G')
n <- 4
size <- 1
replace <- TRUE
prob <- c(0.23,0.27,0.23,0.27)


#generate 20 sequences with label 1 
for(count in 1:30000)
{
    #generate 30 random characters and append (a.k.a paste) it to background_string
    background_string <- ""
    for(i in 1:90)
    {
        c <- sample(x, size, replace, prob)
        background_string <- paste(background_string,c)
    
    }
    
    #string generated above by default has 1 space between each character, so we have to remove all those spaces
    cat("String is: ",background_string,"\n")
    background_string <- str_replace_all(string=background_string, pattern=" ", repl="")
    cat("String after removal of spaces is: ",background_string,"\n")
    
    
    motif <- "GATATGTACC"
    final_string <- ""

    #randomly generated index where motif has to be inserted
    insert_index <- sample(1:90, 1, replace=TRUE)
    cat("Index generated is: ",insert_index,"\n")
    
    
    #substring function used to insert motif
    final_string <- paste(substr(background_string,0,insert_index-1), motif , substr(background_string,insert_index,90))
    final_string <- str_replace_all(string=final_string, pattern=" ", repl="")
    
    cat("Final String is: ",final_string,"\n")
    
    
    #writing sequence and class label to csv file
    df <- data.frame(sequence=final_string, label="1")
    write.table(df, file="/home/samridhi/boatgang/dataset/data.csv", sep=",", row.names=FALSE, col.names=FALSE, append=TRUE)
}

#generate 20 sequences with label 0
for(count in 1:30000)
{
    #generate 34 random characters and append (a.k.a paste) it to background_string
    background_string <- ""
    for(i in 1:100)
    {
      c <- sample(x, size, replace, prob)
      background_string <- paste(background_string,c)
    }
    
    #remove spaces
    background_string <- str_replace_all(string=background_string, pattern=" ", repl="")
    
    #write the sequence + label to the csv file
    df <- data.frame(sequence=background_string, label="0")
    write.table(df, file="/home/samridhi/boatgang/dataset/data.csv", sep = ",",row.names=FALSE, col.names=FALSE, append=TRUE)
}