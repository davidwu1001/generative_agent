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

## generate_task_decomp的bug
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
from Qwen
TOODOOOOOO
arriving at Hobbs Cafe at 07:30am to begin setting up for the Valentine's Day party. (Duration in minutes: 15, minutes left: 45)
  2) Isabella is arranging tables and chairs to create a cozy and intimate atmosphere. (Duration in minutes: 10, minutes left: 35)
  3) Isabella is placing centerpieces and decorations on each table. (Duration in minutes: 10, minutes left: 25)
  4) Isabella is checking the temperature of the food and drinks to ensure they are served at the right temperature. (Duration in minutes: 5, minutes left: 20)
  5) Isabella is greeting and welcoming customers as they arrive. (Duration in minutes: 5, minutes left: 15)
  6) Isabella is taking orders and ensuring that all customers are satisfied with their meals and drinks. (Duration in minutes: 10, minutes left: 5)
  7) Isabella is handling any issues or concerns that may arise during the party. (Duration in minutes: 5, minutes left: 0)
-==- -==- -==- 
TOODOOOOOO
arriving at Hobbs Cafe at 07:30am to begin setting up for the Valentine's Day party. (Duration in minutes: 15, minutes left: 45)
  2) Isabella is arranging tables and chairs to create a cozy and intimate atmosphere. (Duration in minutes: 10, minutes left: 35)
  3) Isabella is placing centerpieces and decorations on each table. (Duration in minutes: 10, minutes left: 25)
  4) Isabella is checking the temperature of the food and drinks to ensure they are served at the right temperature. (Duration in minutes: 5, minutes left: 20)
  5) Isabella is greeting and welcoming customers as they arrive. (Duration in minutes: 5, minutes left: 15)
  6) Isabella is taking orders and ensuring that all customers are satisfied with their meals and drinks. (Duration in minutes: 10, minutes left: 5)
  7) Isabella is handling any issues or concerns that may arise during the party. (Duration in minutes: 5, minutes left: 0)
-==- -==- -==- 
Error.
Enter option: Traceback (most recent call last):
  File "D:\python\generative_agents\reverie\backend_server\reverie.py", line 468, in open_server
    rs.start_server(int_count)
  File "D:\python\generative_agents\reverie\backend_server\reverie.py", line 379, in start_server
    next_tile, pronunciatio, description = persona.move(
  File "D:\python\generative_agents\reverie\backend_server\persona\persona.py", line 222, in move
    plan = self.plan(maze, personas, new_day, retrieved)
  File "D:\python\generative_agents\reverie\backend_server\persona\persona.py", line 148, in plan
    return plan(self, maze, personas, new_day, retrieved)
  File "D:\python\generative_agents\reverie\backend_server\persona\cognitive_modules\plan.py", line 959, in plan
    _determine_action(persona, maze)
  File "D:\python\generative_agents\reverie\backend_server\persona\cognitive_modules\plan.py", line 592, in _determine_action
    generate_task_decomp(persona, act_desp, act_dura))
  File "D:\python\generative_agents\reverie\backend_server\persona\cognitive_modules\plan.py", line 164, in generate_task_decomp
    return run_gpt_prompt_task_decomp(persona, task, duration)[0]
  File "D:\python\generative_agents\reverie\backend_server\persona\prompt_template\run_gpt_prompt.py", line 453, in run_gpt_prompt_task_decomp
    output = safe_generate_response(prompt, gpt_param, 5, get_fail_safe(),
  File "D:\python\generative_agents\reverie\backend_server\persona\prompt_template\gpt_structure.py", line 289, in safe_generate_response
    return func_clean_up(curr_gpt_response, prompt=prompt)
  File "D:\python\generative_agents\reverie\backend_server\persona\prompt_template\run_gpt_prompt.py", line 392, in __func_clean_up
    duration = int(k[1].split(",")[0].strip())
IndexError: list index out of range
```

修改prompt

```
Describe subtasks in 5 min increments. 

---
In 5 min increments, list the subtasks Kelly does when Kelly is working on the next day's kindergarten lesson plan from 09:00am ~ 12:00pm (total duration in minutes: 180).
previous subtasks as follows:
1) Kelly is reviewing the kindergarten curriculum standards. (duration in minutes: 15, minutes left: 165)
2) Kelly is brainstorming ideas for the lesson. (duration in minutes: 30, minutes left: 135)

let's think step by step and List the next item in one sentence:
answer: Kelly is creating the lesson plan. (duration in minutes: 30, minutes left: 105)

let's think step by step and List the next item in one sentence:
answer: Kelly is creating materials for the lesson. (duration in minutes: 30, minutes left: 75)
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
In 5 min increments, list the subtasks Isabella does when Isabella is waking up and completing her morning routine from 06:00AM ~ 07:00AM (total duration in minutes 60).
previous subtasks as follows:
1) getting out of bed. (duration in minutes: 5, minutes left: 55)
2) brushing teeth. (duration in minutes: 5, minutes left: 50)
3) Isabella is taking a shower. (duration in minutes: 10, minutes left: 40)
4) Isabella is drying herself off and getting dressed. (duration in minutes: 10, minutes left: 30)
5) Isabella is making breakfast. (duration in minutes: 10, minutes left: 20)
6) Isabella is doing some light exercise. (duration in minutes: 10, minutes left: 10)
7) Isabella is drinking coffee and reviewing her schedule for the day. (duration in minutes: 5, minutes left: 5)

let's think step by step and List the next item in one sentence:
answer:
```

模板

input7 由Persona first names改为previous items

```
task_decomp_v3.txt

Variables: 
!<INPUT 0>! -- Commonset
!<INPUT 1>! -- Surrounding schedule description
!<INPUT 2>! -- Persona first name
!<INPUT 3>! -- Persona first name
!<INPUT 4>! -- Current action
!<INPUT 5>! -- curr time range
!<INPUT 6>! -- Current action duration in min
!<INPUT 7>! -- previous items


<commentblockmarker>###</commentblockmarker>
Describe subtasks in 5 min increments. 
---
In 5 min increments, list the subtasks Kelly does when Kelly is working on the next day's kindergarten lesson plan from 09:00am ~ 12:00pm (total duration in minutes: 180).
previous subtasks as follows:
1) Kelly is reviewing the kindergarten curriculum standards. (duration in minutes: 15, minutes left: 165)
2) Kelly is brainstorming ideas for the lesson. (duration in minutes: 30, minutes left: 135)

let's think step by step and List the next item in one sentence:
answer: Kelly is creating the lesson plan. (duration in minutes: 30, minutes left: 105)

let's think step by step and List the next item in one sentence:
answer: Kelly is creating materials for the lesson. (duration in minutes: 30, minutes left: 75)
---
!<INPUT 0>!
!<INPUT 1>!
In 5 min increments, list the subtasks !<INPUT 2>! does when !<INPUT 3>! is !<INPUT 4>! from !<INPUT 5>! (total duration in minutes !<INPUT 6>!).
previous subtasks as follows:
!<INPUT 7>!

let's think step by step and List the next item in one sentence:
answer:
```

初始化previous_items数组

minutes_left = (from the task)



new_clean_up() 获取response，返回output

while(minutes_left>0){

​	合成prompt（persona, task, duration, previous_items）

​	新的validate和clean_up函数

​	output= safe...(prompt, vali...)

​	previous_items.append(new_item)

​	minutes_left = 处理previous_items

}