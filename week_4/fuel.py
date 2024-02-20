def main():
    while True:
        try:
            x = (input("Fraction: ")) # Getting the input

            y,z = x.split("/") # Assigning the number to variable y and z
            y,z =float(y),float(z) # Converting the number so that we can perform calculation. We converted to float in try not in else because its easier to handle error 
        except ValueError:
            continue
        else:
            try:
                if y/z * 100 == 100:
                    print("F") #Performing the final task.
                    break
                elif y/z * 100 == 0:
                    print("E")
                    break
                else:
                    print(f"{y/z*100}")
                    break
            except ZeroDivisionError:
                continue


# We can handle two exception like this at one except:
# except (ValueError, ZeroDivisionError):
main()
