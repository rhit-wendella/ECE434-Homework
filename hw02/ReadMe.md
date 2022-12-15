# Homework 2

## Measuring a gpio pin on an Oscilloscope

1. What's the min and max voltage?
**Max voltage was 3.28V and minimum was 0V**

2. What period and frequency is it?
**235.7ms and 4.243Hz**

3. How close is it to 100ms?
**It is 17.85ms off**

4. Why do they differ?
**Because we have to go through bash in order to open the file and write to it.**

5. Run htop and see how much processor you are using.
**3% of the processor is being used.**

6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? Make a table of the fastest values you try and the corresponding period and processor usage. Try using markdown tables: https://www.markdownguide.org/extended-syntax/#tables

| Sleep time | Period |
|------|--------|
| 0.1 | 235.9ms |
| 0.098 | 231.1ms |
| 0.080 | 196.2ms |

7. How stable is the period?
**It is a little unstable**

8. Try launching something like vi. How stable is the period?
**Also is a little unstable**

9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period?
**It only improves it a little bit**

10. Togglegpio.sh uses bash (first line in file). Try using sh. Is the period shorter?
**It is a lot short because sh is faster than bash**

11. What's the shortest period you can get? 

### Results

| Name | Period | Frequency |
|------|--------|-----------|
| Shell Script | 235.9ms | 4.243Hz |
| Python Script| 10.134ms | 98.678Hz |
| C program w/ lseek | 0.0843ms | 11.862kHz |

### Change SSH Port

**I changed my SSH Port to 2022 and then changed it back because of issues**
