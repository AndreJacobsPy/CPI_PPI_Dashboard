library(readxl)
library(tidyverse)

install.packages("ggplot2")
library(ggplot2)

# Read in data
cpi <- read_excel("/Users/andrejacobs/Desktop/price_analysis/CPI_cleaned.xlsx")
head(cpi)

# read in PPI
ppi <- read_excel("/Users/andrejacobs/Desktop/price_analysis/PPI_cleaned.xlsx")
head(ppi)

# look at distribution of data
lower_label <- c()
mid_label <- c()
upper_label <- c()
for (i in cpi$Lower) {
    lower_label <- append(lower_label, "Lower")
    mid_label <- append(mid_label, "Mid")
    upper_label <- append(upper_label, "Upper")
}

name <- append(lower_label, c(mid_label, upper_label))
value <- append(cpi$Lower, c(cpi$Mid, cpi$Upper))

hist_data <- data.frame(name = name, cpi = value)
head(hist_data)

# make the plot
ggplot(hist_data, aes(cpi, fill = name)) +
    geom_histogram(alpha = 0.5, color = "#e6e6e6", bins = 15)


# data is distributed approximately normal
head(cpi)
head(ppi)

mean(cpi$Mid)
mean(ppi$Mid)

t.test(cpi$Lower, ppi$Lower, alternative = "less")$p.value
t.test(cpi$Mid, ppi$Mid, alternative = "less")$p.value
t.test(cpi$Upper, ppi$Upper, alternative = "less")$p.value

cols <- c("Lower", "Mid", "Upper")
t.test(cpi[cols], ppi[cols], alternative = "less")$p.value
