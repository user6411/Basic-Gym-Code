faze = ['preparation', 'lifting', 'lowering', 'break']

for f in faze:
    while True:
        try: 
            entry = int(input('Enter the number of the phase in the exercise: '))

        except ValueError:
            print('Numbers only please!')
            continue
        
        
        
        if entry <= 0 or entry > 4:
            print('You can enter up to 4 phases only and it must be greater than 0!')

            continue

        print(f"You are currently in: {f}")

        break

