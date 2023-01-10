# ece434HW 
> for the ECE434 homework

## 1. HW1: Etch-a-sketch
- Status: done 
- Up - 'w'; Down - 's'; Left - 'a'; Right - 'd'; Clear - 'c'; Exit - esc

## 2. HW2: gpio speed
1. What's the min and max voltage?
    3.343V, 0V
2. What period and frequency is it?
    265ms , 3.7735kHz
3. How close is it to 200ms?
    It is off by 65ms.
4. Why do they differ?
    Bash is still slow 
5. Run htop and see how much processor you are using.
    3%
6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? Make a table of the fastest values you try and the corresponding period and processor usage. Try using markdown tables: https://www.markdownguide.org/extended-syntax/#tables

  | Sleep Time     | Period |
  | ----------- | ----------- |
  | 0.1        | 265ms |
  | 0.098       | 260ms |
  | 0.080        | 245ms |
7. How stable is the period?
    It is a little unstable
8. Try launching something like vi. How stable is the period?
    It is unstable also
9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period?
    It does make it a little fast
10. Togglegpio.sh uses bash (first line in file). Try using sh. Is the period shorter?
    It is faster because sh is faster than bash
11. What's the shortest period you can get?
    35 ms

