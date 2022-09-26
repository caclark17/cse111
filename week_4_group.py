import math
import pytest

def main():
    
    CAN_NAME = 0
    CAN_RADIUS = 1
    CAN_HEIGHT = 2
    CAN_PRICE = 3
    CAN_VOLUME = 4
    CAN_SURFACE_AREA = 5
    CAN_EFF = 6
    CAN_COST_EFF = 7
    
    can_data = [
        ["#1 Picnic",6.83,10.16,0.28],
        ["#1 Tall",7.78,11.91,0.43],
        ["#2",8.73,11.59,0.45],
        ["#2.5",10.32,11.91,0.61],
        ["#3 Cylinder",10.79,17.78,0.86],
        ["#5",13.02,14.29,0.83],
        ["#6Z",5.40,8.89,0.22],
        ["#8Z short",6.83,7.62,0.26],
        ["#10",15.72,17.78,1.53],
        ["#211",6.83,12.38,0.34],
        ["#300",7.62,11.27,0.38],
        ["#303",8.10,11.11,0.42]
        ]
    
    for can in can_data:
        can_volume = compute_volume(can[CAN_RADIUS], can[CAN_HEIGHT])
        can_surface_area = compute_surface_area(can[CAN_RADIUS], can[CAN_HEIGHT])
        can_efficiency = compute_storage_efficiency(can_volume,can_surface_area)
        can_cost_efficiency = compute_cost_efficiency(can_volume, can[CAN_PRICE])
        can.append(can_volume)
        can.append(can_surface_area)
        can.append(can_efficiency)
        can.append(can_cost_efficiency)

    cans_sorted = sorted(can_data, key=lambda x: x[CAN_PRICE], reverse=True)
    
    for can in cans_sorted:
        print(f"{can[CAN_NAME]:15}  {can[CAN_PRICE]:} St. Eff: {can[CAN_EFF]:7.2f}  Cost Eff. {can[CAN_COST_EFF]:7.2f}")

        
    
def compute_cost_efficiency(can_volume, can_cost):
    return can_volume/can_cost
    

def compute_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

def compute_surface_area(radius,height):
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(volume, surface_area):
    efficiency = volume / surface_area
    return efficiency


main()
