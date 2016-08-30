# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

>>top - display a list of processes  
>>screen - terminal multiplexer  
>>grep - pull out lines that match a pattern  
>>cut - split a line by a delimiter and return a specific item  
>>ps - process list  
>>ls - list directory  
>>cd - change directory  
>>sudo - make me a sandwich  
>>ssh - connect to another server  
>>scp - copy file to another server  
>>cp - copy file  
>>mv - move file  
>>sudo rm -rf / - some men just want to watch the world burn  

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

>>list dir  
>>list dir including hidden files  
>>list dir with extra info  
>>list dir with extra info with unit suffixes  
>>list dir including hidden files with extra info using unit suffixes  
>>list dir sorted by modified time  
>>list dir with extra info, colorized with trailing slash for directory  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

>>-1 - 1 line per listing  
>>-m - comma delimited  
>>-L - list symbolic link target  
>>-R - include subdirectories  
>>-d - only directories  

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

>>takes a list of strings and allows you to process them with another command
>>cat somefile.txt | xargs -I% echo blah blah %  

 

