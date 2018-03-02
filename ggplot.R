##to plot a grah that represents spatial differences in reflect of index calculated

index <- read.csv("postcode.csv")
#to make the intex easier to see and compare, increase the value by 100 times
index[,2] <- index[,2]*100

#import the shape file of Yeman Map; 3 shape files, 
#chose the one that has the 22 administrative regions to work with
library(rgdal)
library(dplyr)
library(ggplot2)

ymn <- readOGR(dsn = "yemen_admin_20171007_shape", layer = "yem_admin1")

#join the index calculated to the data in the shape file
ymn@data <- left_join(ymn@data, index, by = "pcode")

#To use ggplot, transform the shape file into dataframe with geo information,
#then merge to the original file 
ymn_t <- broom::tidy(ymn)
ymn$id <- row.names(ymn)
ymn_t <- left_join(ymn_t, ymn@data, by = "id")

map <- ggplot(ymn_t, aes(long, lat, group = group, fill = Score.Index)) +
        geom_polygon() + coord_equal() +
        labs(x = "", y = "",
             fill = "Index score") +
        ggtitle("Severity index of cholera outbreak in Yemen")
map + scale_fill_gradient(low = "#184769", high = "#00e1c6")
