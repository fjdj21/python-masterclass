computer_parts = ["computer",   # 0
                  "monitor",    # 1
                  "keyboard",   # 2
                  "mouse",      # 3
                  "mouse mat"   # 4
                  ]
print(computer_parts)

#computer_parts[3] = 'trackball'
print(computer_parts[3:])

computer_parts[3:] = "trackball"
print(computer_parts)

computer_parts[3:] = ['trackball']
print(computer_parts)
