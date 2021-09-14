
## Measure when most changes occured ##


#data used: readability_sample1, I open directly the rda file
setwd("I:\\!Hiwis\\f-kraeme\\sample_filled_new")
load(file = "readabilityscores.rda")

#creating a year/qtr parameter from character 
first_col <- as.Date(readabilityscores$date, format="%Y-%m-%d")

#changing data a bit

#same firm identifier per undertaking
readabilityscores$`firm identifier` <- gsub("\\.(?:.(?!\\.))+$","", readabilityscores$`firm identifier`, perl=TRUE)

withoutnas <- na.omit(readabilityscores) #getting rid of all nas

###creating dummy variable ###
#for loops that marks differences with 1

#for NAs
for (i in 1:nrow(readabilityscores)){
  if(is.na(readabilityscores$'nWS score'[i]) == TRUE){
    readabilityscores$change[i] <- 0
  } else if(identical(readabilityscores$'nWS score'[i-1], readabilityscores$'nWS score'[i]) != TRUE && is.na(readabilityscores$'nWS score'[i-1]) == FALSE) {
    readabilityscores$change[i] <- 1
  }  else {
    readabilityscores$change[i] <- 0
  }
  
}



#without NAs
for (i in 1:nrow(withoutnas)){
  if(identical(withoutnas$'nWS score'[i-1], withoutnas$'nWS score'[i]) != TRUE && identical(withoutnas$`firm identifier`[i],withoutnas$`firm identifier`[i-1]) == TRUE) {
    withoutnas$change[i] <- 1
  }  else {
    withoutnas$change[i] <- 0
  }
  
}


#saving file 
write.csv(withoutnas,"I:\\!Hiwis\\f-kraeme\\Internship\\readability_sample_withoutnas_with_score.csv", row.names = FALSE)


#creating a frequency table of the changes
g <- example %>% group_by(date,change) %>% summarise(N=n())

