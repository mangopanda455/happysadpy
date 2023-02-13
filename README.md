# happysadpy

There is a loop that can be used to determine whether a number is happy or sad. The way it goes is essentially (m being the number you want to determine the happiness of):

<img width="348" alt="Screenshot 2023-02-13 at 8 46 57 AM" src="https://user-images.githubusercontent.com/115837698/218474725-ea93a85a-1c4a-4e6b-b8d2-f237fd010ea4.png">

The explanation for this is as follows: The number (m) that you want to determine the hapiness status of is first squared. Then, the number produced is split into it's digits (m<sub>1</sub>, m<sub>2</sub>). If the produced number is one digit, it stays the same and is just itself for the next steps, and if it is more than 2 digits, then those digits are also used for the following steps (the digits can be denoted as m<sub>3</sub>, m<sub>4</sub>, etc). The next step is squaring all of the digits that have been split up. So in the case above m<sub>1</sub> and m<sub>2</sub> are squared. Then, those two numbers produced from the previous step are summed, and I have denoted the final number produced as n. This process is continued until:

1. n becomes 1, then all the next iterations will keep n at 1
2. n never reaches 1, and goes in an infinite loop, never reaching 1

A number is happy if it eventually reaches one, like in the first scenario, and a number is sad if it never reaches 1, and keeps looping, like in the second scenario. To make this a bit simpler, here is this scenario with the number 7:

<img width="706" alt="Screenshot 2023-02-13 at 8 49 05 AM" src="https://user-images.githubusercontent.com/115837698/218475170-53c07fb3-d668-4539-9119-976eca121478.png">

Now that we have gotten to 1 after doing the cycle over and over, we can confidently say that 7 is a happy number. Now lets do it with a number like 2:

<img width="726" alt="Screenshot 2023-02-13 at 8 49 29 AM" src="https://user-images.githubusercontent.com/115837698/218475257-3a61b73b-d17a-4aa2-8a36-73a1e4a4a11f.png">
