test_scores= [int(i) for i in input("Enter the test scores:").split()]

print("Highest score is:", max(test_scores))
print("Lowest score is:",min(test_scores))
if max(test_scores) > 100:
    print("A value over 100 has been entered")   
else:
   print("Average score is ",sum(test_scores)/len(test_scores))
   test_scores.sort()
   print("Second largest score is:",test_scores[-2])
   print(test_scores)
   test_scores.pop(0)
   test_scores.pop(0)
   print("Drop:", test_scores)
   print("Average score is ",sum(test_scores)/len(test_scores))