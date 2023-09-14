def calculate_circle_area_and_perimeter(radius):
    pi=3.14159
    area=pi*radius**2
    perimeter=2*pi*radius
    return area, perimeter

def calculate_rectangle_area_and_perimeter(length, width):
    area=length*width
    perimeter=2*(width+length)
    return area, perimeter

def calculate_triangle_area_and_perimeter(side1, side2, side3):
    s=(side1+side2+side3)/2
    area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
    perimeter=side1+side2+side3
    return area, perimeter
    
def main():
    while True:
        print("請選擇一個圖形")
        print("1.圓形\n2.矩形\n3.三角形\n4.退出程式")
        
        choice=input("請輸入選項(1/2/3/4):")
        
        if choice=='1':
            radius=float(input("請輸入圓的半徑:"))
            if radius>0:
                area, perimeter=calculate_circle_area_and_perimeter(radius)
                print(f"面積:{area:.2f}")
                print(f"周長:{perimeter:.2f}\n")
            else :
                print("半徑不能為零或是負的，請再式一次")
        
        if choice=='2':
            length=float(input("請輸入矩形的長:"))
            width=float(input("請輸入矩形的寬:"))
            if length and width>0:
                area, perimeter=calculate_rectangle_area_and_perimeter(length, width)
                print(f"面積:{area:.2f}")
                print(f"周長:{perimeter:.2f}\n")
            else :
                print("長和寬不能為零或是負的，請再式一次")
        
        if choice=='3':
            side1=float(input("請輸入三角形的邊長一:"))
            side2=float(input("請輸入三角形的邊長二:")) 
            side3=float(input("請輸入三角形的邊長三:"))
            if side1 and side2 and side3>0:
                if side1+side2>side3 and side1+side3>side2 and side3+side2>side1:
                    area, perimeter=calculate_triangle_area_and_perimeter(side1, side2, side3)
                    print(f"面積:{area:.2f}")
                    print(f"周長:{perimeter:.2f}\n")
                else :
                    print("此三角形不成立，請再式一次")
            else :
                print("邊長不能為零或是負的，請再式一次")
        
        if choice=='4':
            print("感謝使用，再見!")
            break
        
if __name__=="__main__":
    main()