# Public BugBounty Programs Watcher
chaosWatcher is a program to view the changes made on the bug bounty programs listed on https://chaos.projectdiscovery.io/, which finds the changes in time intervals according to its execution.


## How to use?
1. Run the program for the first time
```bash
python3 chaosWatcher.py
```
2. The program will download and save the json object from [chaos-bugbounty-list](https://github.com/projectdiscovery/public-bugbounty-programs/blob/main/chaos-bugbounty-list.json) in the current directory (**Don't remove the corresponding file unless you want to reset the time interval**)
3. Run the program again in time intervals to watch for any changes in the list and print out the result for you.

*Currently, the program watches for the addition and the deletion of the program and program bounty and domains.*


## Example
- When the program run for the first time -> [bac3e8](https://raw.githubusercontent.com/projectdiscovery/public-bugbounty-programs/bac3e8c55d0b0cc0c6c3edc4ddf923ec10739066/chaos-bugbounty-list.json)
- When the program run for the second time -> [b5106a](https://raw.githubusercontent.com/projectdiscovery/public-bugbounty-programs/b5106ada7162a8c0178c223aab64790c9205e467/chaos-bugbounty-list.json)

- Output of second time:

  ```
  $ python3 chaosWatcher.py                                                                                                                             
  
  New program:

  Name: Coinspot
  URL: https://hackerone.com/coinspot?type=team
  Offers Bounty?: True
  domains: ['coinspot.com.au']
  
  Changes has been made to Comcast Xfinity program:
  Program bounty has been changed to True
  
  Database Updated!
  ```
