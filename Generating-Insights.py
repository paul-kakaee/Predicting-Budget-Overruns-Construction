def generate_insights(coefficients):
    insights = []
    for feature, coef in coefficients['Coefficient'].items():
        if coef > 0:
            insights.append(f'Increasing {feature} leads to an increase in project duration.')
        else:
            insights.append(f'Increasing {feature} leads to a decrease in project duration.')
    return insights

insights = generate_insights(coefficients)
print("Insights based on the analysis:")
for insight in insights:
    print(insight)
