import pandas as pd
from plotnine import ggplot, aes, geom_line, labs, theme_minimal
from plotnine.data import economics

# Load the dataset
df = economics

plot_pop = (
    ggplot(df) +
    aes(x='date', y='pop') +
    geom_line(color='blue') +
    labs(title='US Population Over Time', x='Date', y='Population') +
    theme_minimal()
)
print(plot_pop)
plot_unemploy = (
    ggplot(df) +
    aes(x='date', y='unemploy') +
    geom_line(color='red') +
    labs(title='Unemployment Over Time', x='Date', y='Unemployed Persons') +
    theme_minimal()
)
print(plot_unemploy)

plot_psavert = (
    ggplot(df) +
    aes(x='date', y='psavert') +
    geom_line(color='green') +
    labs(title='Personal Savings Rate Over Time', x='Date', y='Savings Rate (%)') +
    theme_minimal()
)
print(plot_psavert)
