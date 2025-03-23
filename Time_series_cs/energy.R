library(readxl)
library(lubridate)
energy <- read_excel("./energy.xlsx")
btc <- readxl::read_excel(paste0(getwd(), "/energy.xlsx"), skip = 10)
btc$year <- year(btc$Month)
btc$month <- month(btc$Month)
btc <- btc[-1,]
all.energy <- ts(btc[,"Electricity Sales to Ultimate Customers in the Industrial Sector"], frequency=12, start=c(btc$year[1],btc$month[1]))

plot(all.energy)

library(TSstudio)
energy.new <- TSstudio::ts_split(all.energy, sample.out = 24)
Time <- time(energy.new$train)
Seas <- cycle(energy.new$train)
Seas <- as.factor(Seas)
model <- lm()
summary(model)

View(all.energy)

