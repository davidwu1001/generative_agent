 - TOKEN LIMIT EXCEEDED
千问大模型的长度超限了
```
Describe subtasks in 5 min increments. 
---
Name: Kelly Bronson
Age: 35
Backstory: Kelly always wanted to be a teacher, and now she teaches kindergarten. During the week, she dedicates herself to her students, but on the weekends, she likes to try out new restaurants and hang out with friends. She is very warm and friendly, and loves caring for others.
Personality: sweet, gentle, meticulous
Location: Kelly is in an older condo that has the following areas: {kitchen, bedroom, dining, porch, office, bathroom, living room, hallway}.
Currently: Kelly is a teacher during the school year. She teaches at the school but works on lesson plans at home. She is currently living alone in a single bedroom condo.
Daily plan requirement: Kelly is planning to teach during the morning and work from home in the afternoon.s
Today is Saturday May 10. From 08:00am ~09:00am, Kelly is planning on having breakfast, from 09:00am ~ 12:00pm, Kelly is planning on working on the next day's kindergarten lesson plan, and from 12:00 ~ 13pm, Kelly is planning on taking a break. 
In 5 min increments, list the subtasks Kelly does when Kelly is working on the next day's kindergarten lesson plan from 09:00am ~ 12:00pm (total duration in minutes: 180):
1) Kelly is reviewing the kindergarten curriculum standards. (duration in minutes: 15, minutes left: 165)
2) Kelly is brainstorming ideas for the lesson. (duration in minutes: 30, minutes left: 135)
3) Kelly is creating the lesson plan. (duration in minutes: 30, minutes left: 105)
4) Kelly is creating materials for the lesson. (duration in minutes: 30, minutes left: 75)
5) Kelly is taking a break. (duration in minutes: 15, minutes left: 60)
6) Kelly is reviewing the lesson plan. (duration in minutes: 30, minutes left: 30)
7) Kelly is making final changes to the lesson plan. (duration in minutes: 15, minutes left: 15)
8) Kelly is printing the lesson plan. (duration in minutes: 10, minutes left: 5)
9) Kelly is putting the lesson plan in her bag. (duration in minutes: 5, minutes left: 0)
---
Name: Isabella Rodriguez
Age: 34
Innate traits: friendly, outgoing, hospitable
Learned traits: Isabella Rodriguez is a cafe owner of Hobbs Cafe who loves to make people feel welcome. She is always looking for ways to make the cafe a place where people can come to relax and enjoy themselves.
Currently: Status: Today is the day! Isabella Rodriguez is filled with excitement as the Valentine's Day party at Hobbs Cafe is finally here. She has been tirelessly planning and preparing for this event, and now it's time to bring it to life. The party is set to start at 5pm at Hobbs Cafe, and Isabella has ensured that everything is carefully arranged and ready to create a memorable evening for everyone. She can't wait to welcome her customers and friends to join the festivities and celebrate love together. Isabella is confident that her efforts will pay off and that the party will be a great success.
Lifestyle: Isabella Rodriguez goes to bed around 11pm, awakes up around 6am.
Daily plan requirement: 1. Wake up at 6am and complete morning routine (shower, brush teeth, get dressed) by 6:30am. 2. Arrive at Hobbs Cafe by 7:30am to do final preparations for the Valentine's Day party. 3. Welcome and greet customers as they arrive for the party starting at 5pm. 4. Ensure that food and drinks are well-stocked and available throughout the evening. 5. Continuously check on guests and provide excellent customer service during the event. 6. Close the cafe at 8pm and do a final walkthrough to ensure everything is in order before heading home.
Current Date: Tuesday February 14
Today is February 14, 2023. From 07:00AM ~ 08:00AM, Isabella Rodriguez is planning on arriving at Hobbs Cafe to do final preparations for the Valentine's Day party, 08:00AM ~ 09:00AM, Isabella Rodriguez is planning on opening Hobbs Cafe and attending to guests, 09:00AM ~ 10:00AM, Isabella Rodriguez is planning on having lunch with her staff.
In 5 min increments, list the subtasks Isabella does when Isabella is opening Hobbs Cafe and attending to guests from 08:00AM ~ 09:00AM (total duration in minutes 60): 
1) Isabella is
```
- openai的embedding还是需要的openai的api-key
embedding是将文本生成词向量，这就矛盾了
设置一个Qwen的请求和gpt的请求，分开配置

- [ ]  生成起床时间 需要的结果是6am，但是千问的回答是Isabella Rodriguez wakes up around 6am.
修改prompt
- [ ] 生成小时计划的时候，如何避免他一直续写下去，而只专注于6am

## 对于generate_task_decomp的bug
如果用原来的one-shot prompt 只有很小的概率输出正确的格式
target:
```commandline
Describe subtasks in 5 min increments. 
---
Name: Kelly Bronson
Age: 35
Backstory: Kelly always wanted to be a teacher, and now she teaches kindergarten. During the week, she dedicates herself to her students, but on the weekends, she likes to try out new restaurants and hang out with friends. She is very warm and friendly, and loves caring for others.
Personality: sweet, gentle, meticulous
Location: Kelly is in an older condo that has the following areas: {kitchen, bedroom, dining, porch, office, bathroom, living room, hallway}.
Currently: Kelly is a teacher during the school year. She teaches at the school but works on lesson plans at home. She is currently living alone in a single bedroom condo.
Daily plan requirement: Kelly is planning to teach during the morning and work from home in the afternoon.s

Today is Saturday May 10. From 08:00am ~09:00am, Kelly is planning on having breakfast, from 09:00am ~ 12:00pm, Kelly is planning on working on the next day's kindergarten lesson plan, and from 12:00 ~ 13pm, Kelly is planning on taking a break. 
In 5 min increments, list the subtasks Kelly does when Kelly is working on the next day's kindergarten lesson plan from 09:00am ~ 12:00pm (total duration in minutes: 180):
1) Kelly is reviewing the kindergarten curriculum standards. (duration in minutes: 15, minutes left: 165)
2) Kelly is brainstorming ideas for the lesson. (duration in minutes: 30, minutes left: 135)
3) Kelly is creating the lesson plan. (duration in minutes: 30, minutes left: 105)
4) Kelly is creating materials for the lesson. (duration in minutes: 30, minutes left: 75)
5) Kelly is taking a break. (duration in minutes: 15, minutes left: 60)
6) Kelly is reviewing the lesson plan. (duration in minutes: 30, minutes left: 30)
7) Kelly is making final changes to the lesson plan. (duration in minutes: 15, minutes left: 15)
8) Kelly is printing the lesson plan. (duration in minutes: 10, minutes left: 5)
9) Kelly is putting the lesson plan in her bag. (duration in minutes: 5, minutes left: 0)
---
Name: Isabella Rodriguez
Age: 34
Innate traits: friendly, outgoing, hospitable
Learned traits: Isabella Rodriguez is a cafe owner of Hobbs Cafe who loves to make people feel welcome. She is always looking for ways to make the cafe a place where people can come to relax and enjoy themselves.
Currently: Isabella Rodriguez is planning on having a Valentine's Day party at Hobbs Cafe with her customers on February 14th, 2023 at 5pm. She is gathering party material, and is telling everyone to join the party at Hobbs Cafe on February 14th, 2023, from 5pm to 7pm.
Lifestyle: Isabella Rodriguez goes to bed around 11pm, awakes up around 6am.
Daily plan requirement: Isabella Rodriguez opens Hobbs Cafe at 8am everyday, and works at the counter until 8pm, at which point she closes the cafe.
Current Date: Monday February 13

Today is February 13, 2023. From 00:00AM ~ 06:00AM, Isabella Rodriguez is planning on sleeping, 06:00AM ~ 07:00AM, Isabella Rodriguez is planning on waking up and completing her morning routine, 07:00AM ~ 09:00AM, Isabella Rodriguez is planning on opening Hobbs Cafe.
In 5 min increments, list the subtasks Isabella does when Isabella is waking up and completing her morning routine from 06:00AM ~ 07:00AM (total duration in minutes 60): 
1) Isabella is 

-------------------------------------------
waking up and getting out of bed. (duration in minutes: 5, minutes left: 55)
  2) Isabella is brushing her teeth and washing her face. (duration in minutes: 10, minutes left: 45)
  3) Isabella is getting dressed. (duration in minutes: 10, minutes left: 35)
  4) Isabella is doing her hair and makeup. (duration in minutes: 15, minutes left: 20)
  5) Isabella is making coffee and tea for herself and her staff. (duration in minutes: 10, minutes left: 10)
  6) Isabella is checking her emails and messages. (duration in minutes: 5, minutes left: 5)
  7) Isabella is reviewing the schedule for the day. (duration in minutes: 5, minutes left: 0)
```
exp1
```commandline
1) Isabella is brushing her teeth and washing her face for 5 minutes.
  2) Isabella is getting dressed and doing her hair for 10 minutes.
  3) Isabella is making her bed and tidying her room for 10 minutes.
  4) Isabella is brewing coffee and setting up the cafe for the day for 15 minutes.
  5) Isabella is reviewing the menu and ensuring all ingredients are fresh for 10 minutes.
  6) Isabella is practicing some self-care, such as meditation or exercise for 10 minutes.
  7) Isabella is reviewing any messages or emails for the cafe for 5 minutes.
  8) Isabella is checking the weather forecast and preparing accordingly for the party on February 14th, 2023 at 5pm. (e.g., if it's going to rain, she'll need to prepare a covered outdoor area) for 10 minutes.
```
exp2
```commandline
1) Brushing teeth - 5 minutes
  2) Taking a shower - 10 minutes
  3) Getting dressed - 10 minutes
  4) Doing hair and makeup - 15 minutes
  5) Preparing coffee - 10 minutes
  6) Eating breakfast - 10 minutes
  7) Checking emails and social media - 10 minutes
  8) Packing lunch and any necessary items for work - 10 minutes
  9) Setting reminders for important tasks or appointments - 5 minutes
  10) Doing some light stretching or exercise - 5 minutes.
```
exp3
```commandline
I'm sorry, it seems like your question was cut off. Could you please provide me with the complete information so I can assist you better?

```
exp4
```commandline
waking up and getting out of bed (5 min)
2) Isabella is brushing her teeth (5 min)
3) Isabella is washing her face (5 min)
4) Isabella is doing some light stretching (5 min)
5) Isabella is getting dressed (5 min)
6) Isabella is preparing her hair and makeup (10 min)
7) Isabella is setting the table for the cafe (10 min)
8) Isabella is checking inventory and restocking supplies (10 min)
9) Isabella is reviewing the daily schedule and making any necessary preparations (10 min)
10) Isabella is taking a moment to meditate and center herself before starting her day (5 min)
Total duration: 60 minutes.
```
exp5
```commandline
brushing her teeth (duration in minutes: 5, minutes left: 55) 2) Isabella is washing her face (duration in minutes: 5, minutes left: 50) 3) Isabella is getting dressed (duration in minutes: 10, minutes left: 40) 4) Isabella is doing her hair (duration in minutes: 10, minutes left: 30) 5) Isabella is applying makeup (duration in minutes: 10, minutes left: 20) 6) Isabella is making coffee (duration in minutes: 5, minutes left: 15) 7) Isabella is setting up the cafe (duration in minutes: 5, minutes left: 10) 8) Isabella is reviewing the menu for the day (duration in minutes: 5, minutes left: 5) 9) Isabella is checking her phone for messages or reservations (duration in minutes: 5, minutes left: 0)
```
把prompt改成更简短的one-shot
```commandline
task: Describe subtasks in 5 min increments.

Name: Isabella Rodriguez
Age: 34
Innate traits: friendly, outgoing, hospitable
Learned traits: Isabella Rodriguez is a cafe owner of Hobbs Cafe who loves to make people feel welcome. She is always looking for ways to make the cafe a place where people can come to relax and enjoy themselves.
Currently: Isabella Rodriguez is planning on having a Valentine's Day party at Hobbs Cafe with her customers on February 14th, 2023 at 5pm. She is gathering party material, and is telling everyone to join the party at Hobbs Cafe on February 14th, 2023, from 5pm to 7pm.
Lifestyle: Isabella Rodriguez goes to bed around 11pm, awakes up around 6am.
Daily plan requirement: Isabella Rodriguez opens Hobbs Cafe at 8am everyday, and works at the counter until 8pm, at which point she closes the cafe.
Current Date: Monday February 13

output format:
6) Kelly is reviewing the lesson plan. (duration in minutes: 30, minutes left: 30)
7) Kelly is making final changes to the lesson plan. (duration in minutes: 15, minutes left: 15)
8) Kelly is printing the lesson plan. (duration in minutes: 10, minutes left: 5)
9) Kelly is putting the lesson plan in her bag. (duration in minutes: 5, minutes left: 0)

Today is February 13, 2023. From 00:00AM ~ 06:00AM, Isabella Rodriguez is planning on sleeping, 06:00AM ~ 07:00AM, Isabella Rodriguez is planning on waking up and completing her morning routine, 07:00AM ~ 09:00AM, Isabella Rodriguez is planning on opening Hobbs Cafe.
In 5 min increments, list the subtasks Isabella does when Isabella is waking up and completing her morning routine from 06:00AM ~ 07:00AM:

requirement:
total duration in minutes 60

outputs:
1) Isabella is
```
exp1
```commandline
waking up at 6am, (duration in minutes: 10, minutes left: 50)
2) Isabella is brushing her teeth and washing her face, (duration in minutes: 10, minutes left: 40)
3) Isabella is getting dressed, (duration in minutes: 10, minutes left: 30)
4) Isabella is doing some light stretching and exercises, (duration in minutes: 10, minutes left: 20)
5) Isabella is making herself a cup of coffee or tea, (duration in minutes: 10, minutes left: 10)
6) Isabella is checking her phone and emails, (duration in minutes: 10, minutes left: 0)
```
exp2
```commandline
waking up from sleep (duration in minutes: 5, minutes left: 55) 2) Isabella is brushing her teeth (duration in minutes: 5, minutes left: 50) 3) Isabella is washing her face (duration in minutes: 5, minutes left: 45) 4) Isabella is getting dressed (duration in minutes: 10, minutes left: 35) 5) Isabella is doing some light stretching (duration in minutes: 5, minutes left: 30) 6) Isabella is brewing herself a cup of coffee (duration in minutes: 5, minutes left: 25) 7) Isabella is setting the table for the day (duration in minutes: 10, minutes left: 15) 8) Isabella is reviewing her daily schedule (duration in minutes: 5, minutes left: 10) 9) Isabella is checking if there is anything else that needs to be done before opening the cafe (duration in minutes: 5, minutes left: 5)
```
exp3
```commandline
waking up from sleep. (duration in minutes: 5, minutes left: 55) 2) Isabella is getting out of bed. (duration in minutes: 5, minutes left: 50) 3) Isabella is stretching and doing some light exercise. (duration in minutes: 10, minutes left: 40) 4) Isabella is taking a shower and getting ready for the day. (duration in minutes: 15, minutes left: 25) 5) Isabella is brushing her teeth and getting dressed. (duration in minutes: 10, minutes left: 15) 6) Isabella is preparing breakfast for herself and her staff. (duration in minutes: 10, minutes left: 5) 7) Isabella is tidying up her living space and checking her schedule for the day. (duration in minutes: 5, minutes left: 0)
```
exp4
```commandline
waking up from sleep. (Duration: 5 minutes)
2) Isabella is stretching her body. (Duration: 5 minutes)
3) Isabella is brushing her teeth. (Duration: 5 minutes)
4) Isabella is washing her face. (Duration: 5 minutes)
5) Isabella is taking a shower. (Duration: 10 minutes)
6) Isabella is blow-drying her hair. (Duration: 10 minutes)
7) Isabella is getting dressed. (Duration: 10 minutes)
8) Isabella is applying makeup. (Duration: 10 minutes)
9) Isabella is preparing breakfast. (Duration: 10 minutes)
10) Isabella is eating breakfast. (Duration: 10 minutes)
11) Isabella is checking her phone for messages and emails. (Duration: 10 minutes)
12) Isabella is doing some light cleaning around the house. (Duration: 10 minutes)
13) Isabella is reviewing the lesson plan. (Duration: 15 minutes)
14) Isabella is making final changes to the lesson plan. (Duration: 15 minutes)
15) Isabella is printing the lesson plan. (Duration: 10 minutes)
16) Isabella is putting the lesson plan in her bag. (Duration: 5 minutes)
```
exp5
```commandline
awaking up from sleep at 6am. (Duration: 5min, Minutes Left: 55)
2) Isabella is brushing her teeth and getting dressed. (Duration: 10min, Minutes Left: 45)
3) Isabella is taking a shower and washing her hair. (Duration: 15min, Minutes Left: 30)
4) Isabella is blow-drying her hair and applying makeup. (Duration: 15min, Minutes Left: 15)
5) Isabella is making breakfast for herself and her staff. (Duration: 15min, Minutes Left: 0)
6) Isabella is reviewing the lesson plan. (Duration: 30min, Minutes Left: 30)
7) Kelly is making final changes to the lesson plan. (Duration: 15min, Minutes Left: 15)
8) Kelly is printing the lesson plan. (Duration: 10min, Minutes Left: 5)
9) Kelly is putting the lesson plan in her bag. (Duration: 5min, Minutes Left: 0)
```
exp6
```commandline
waking up at 6am, which takes 5 minutes. 2) Isabella is brushing her teeth and washing her face for 5 minutes. 3) Isabella is getting dressed for work, which takes 10 minutes. 4) Isabella is making breakfast for herself and any guests at the cafe, which takes 10 minutes. 5) Isabella is setting the table for breakfast, which takes 5 minutes. 6) Isabella is listening to some music or a podcast for relaxation before starting her workday, which takes 5 minutes. 7) Isabella checks her emails and messages for any important updates or orders, which takes 5 minutes. 8) Isabella reviews the previous day's sales and inventory, which takes 5 minutes. 9) Isabella makes sure that everything is clean and organized for the new day, which takes 5 minutes.

```

exp1
```commandline
waking up from sleep. (duration in minutes: 5, minutes left: 55)
2) Isabella is stretching and doing some light exercise to get her blood flowing. (duration in minutes: 5, minutes left: 50)
3) Isabella is brushing her teeth and washing her face. (duration in minutes: 5, minutes left: 45)
4) Isabella is getting dressed for work. (duration in minutes: 10, minutes left: 35)
5) Isabella is fixing her hair and applying makeup if needed. (duration in minutes: 10, minutes left: 25)
6) Isabella is brewing herself a cup of coffee or tea. (duration in minutes: 5, minutes left: 20)
7) Isabella is reviewing her schedule for the day and making any necessary preparations. (duration in minutes: 10, minutes left: 10)
8) Isabella is checking her emails and responding to any urgent messages. (duration in minutes: 5, minutes left: 5)
9) Isabella is finishing up any remaining tasks before heading out to open the cafe. (duration in minutes: 5, minutes left: 0)
```
exp2
```commandline
Isabella Rodriguez is waking up and completing her morning routine from 06:00AM ~ 07:00AM. Here are the subtasks she does:

  1. Isabella checks the time and sets an alarm if necessary.
  2. Isabella stretches and performs some light exercises to wake up her body.
  3. Isabella takes a shower or bath to freshen up.
  4. Isabella brushes her teeth and gets dressed.
  5. Isabella makes herself a cup of coffee or tea to start her day.
  6. Isabella reviews her schedule for the day and prepares mentally for her tasks.
  7. Isabella packs any necessary items for the day, such as work clothes or lunch.
  8. Isabella checks her emails and social media accounts if she has time.
  9. Isabella reviews her budget and finances for the month to ensure everything is in order.
  10. Isabella checks the weather forecast and plans accordingly for the day.

These subtasks take approximately 60 minutes to complete, leaving her with 0 minutes left in her morning routine before opening the cafe at 09:00AM.
```