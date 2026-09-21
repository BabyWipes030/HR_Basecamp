gizmoAmount = int(input("Number of Gizmos: "))
widgetAmount = int(input("Number of Widgets: "))

def weightCalculator(gizmoAmount, widgetAmount):
    widgetWeight = 75
    gizmoWeight = 112
    totalWeight = (widgetAmount * widgetWeight) + (gizmoAmount * gizmoWeight)
    return print(f"The total weight of the Order: {totalWeight} grams")

weightCalculator(widgetAmount, gizmoAmount)