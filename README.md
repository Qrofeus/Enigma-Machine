# Enigma Machine (Console - Local)

Based on the widely known ciphering technique used in World War II, this implementation uses Python to achieve the functioning of an Enigma Machine. This console based impression of the Enigma Machine, uses a code-book to create unique ciphering setups for each day. There is also a provision for [private-messages](#private-messages) which special [private-codes](data/README.md#3-private-messages) to cipher messages. All ciphering [presets](data/README.md#2-date-presets) and ingredients used in the private-code are stored locally in the user's computer.

An explanation of how all the components in the Enigma Machine work and are implemented in Python can be found in the [components](components/README.md) directory.

## Ciphering Messages

Whenever you run the program, the virtual Enigma Machine will be set using the presets defined for today's date. You can cipher a message using the `message` command in the console. More commands [below](#commands).

```commandline
Enter your command:
> message
Type your message:
There was something beautiful in his hate. It wasn't the hate itself as it was a disgusting display of racism and intolerance. It was what propelled the hate and the fact that although he had this hate, he didn't understand where it came from. It was at that moment that she realized that there was hope in changing him.
>> Ciphered message:
Iytgc top vpzsobzwm tshiavvxd bc rxx okrl. Lo ycqa'o ajr mres dvrxti zm ez ueb m buecovwgub wdnhwcq zr unfatd qgn rdxqhoeiuro. Mn ndg svva cecxhcmgo hlc bmfd foi vwk owrm ymvr hbnmgzus yk pqu wzco ipvq, fr zqkz'y pvaycpzlqp lkmcn hc gxcu vzkr. Er imc ld bdco ufuwoa sfqs jna otknuyxc unhl lsxek boq ucil sb qbfyoyhj lqr.
```

Copy the ciphered message and send it to the intended recipient. When trying to decipher the message, make sure that the machine is set up for the same date as of the ciphered message.
- Use `get-date` command to check the date setup for the Enigma Machine.
- Use `message` command again using the ciphered message for the input, to get the original message back.

```commandline
Enter your command:
> get-date
>> Current machine date: 2023-06-25
----------------------------------------------------------------------------------------------------
Enter your command:
> message
Type your message:
Iytgc top vpzsobzwm tshiavvxd bc rxx okrl. Lo ycqa'o ajr mres dvrxti zm ez ueb m buecovwgub wdnhwcq zr unfatd qgn rdxqhoeiuro. Mn ndg svva cecxhcmgo hlc bmfd foi vwk owrm ymvr hbnmgzus yk pqu wzco ipvq, fr zqkz'y pvaycpzlqp lkmcn hc gxcu vzkr. Er imc ld bdco ufuwoa sfqs jna otknuyxc unhl lsxek boq ucil sb qbfyoyhj lqr.
>> Ciphered message:
There was something beautiful in his hate. It wasn't the hate itself as it was a disgusting display of racism and intolerance. It was what propelled the hate and the fact that although he had this hate, he didn't understand where it came from. It was at that moment that she realized that there was hope in changing him.
```

Use [logs](data/README.md#5-logs) to check ciphered messages and their corresponding dates. Logs pose a security risk if exposed as they contain the both the message and the means to get the presets for that ciphered message. Although, if the logs alone are leaked, it will not compromise the credibility of the EnigmaMachine. To disable logs for the current session, use `no-logs` command.

## Private Messages

Messages can be ciphered with a [private-code](data/README.md#3-private-messages). These codes create a specific machine setup to cipher the input message. These codes work irrespective of the date for the Enigma Machine was previously set to.

When starting out, no private-code will be set for the Enigma Machine. To check the private-code active for the next message use the `code` command in the console. When no such private-code is active `None` will be displayed.

```commandline
Enter your command:
> code
>> Active code: None
```

To set a private-code for your next cipher, use the `private` command and enter an 8 (eight) letter code. Private-codes will only work for one message cipher, after that the Enigma Machine will be reset to the last set date.

```commandline
Enter your command:
> private
Private Code: JNHSIKPW
----------------------------------------------------------------------------------------------------
Enter your command:
> code
>> Active code: JNHSIKPW
```

After a private-code is set, use the `message` command to cipher the private-message. When sending the private-message to someone else, send the private-code used and the ciphered message. When trying to decipher this message, follow the same procedure used to cipher that message.

- Use `private` command to set an 8 letter private-code.
- Check the active private-code using the `code` command.
- Use `message` command to cipher your message.

## How to run

Clone the Enigma-Machine project

```commandline
  git clone https://github.com/Qrofeus/Enigma-Machine
```

Go to the project directory

```commandline
  cd Enigma-Machine
```

Run main.py file using Python

```commandline
  python main.py
```

A command-line program will be run in your console window of a virtual Enigma Machine. Make use of the commands mentioned in this document to use the Enigma Machine.

## Commands

1. `help`\
   Lists out all the commands and their respective actions in the console window.
2. `no-logs`\
   Disables the [logging](data/README.md#5-logs) of ciphered messages for the current session.
3. `get-date`\
   Prints the date for which the Enigma Machine is set to.
4. `set-date`\
   Using the appropriate format(YYYYMMDD or YYYY-MM-DD), change the [presets](data/README.md#2-date-presets) for the Enigma Machine to the input date.
5. `private`\
   Set a [private-code](data/README.md#3-private-messages) for the next message that will be ciphered.
6. `code`\
   Displays the active private-code.
7. `message`\
   Enter the message you wish to cipher in the console window, that message will be ciphered according to the set conditions of the Enigma Machine.
8. `random`\
   Prints out a random paragraph selected from the [database](data/README.md#4-test-paragraphs).
9. `exit/quit`\
   Close the Enigma Machine program.

## Comments

- To better understanding the workings of the Enigma Machine refer to the following YouTube videos:
  - [Numberphile](https://youtu.be/G2_Q9FoD-oQ) where Dr. James Grime demonstrates the actual machine used in the World War II to send coded messages and discusses its many configurations.
  - [Jared Owens](https://youtu.be/ybkkiGtJmkM), A 3D model created of the Enigma Machines used during the war, explained with animations helps in the understanding of the machine.
- In a follow-up video by Numberphile titled [Flaw in the Enigma Code - Numberphile](https://youtu.be/V4V2bpZlqx8), Dr. James discusses the inability of the Enigma Machine to output the same character as the input character.While I have not specifically tested for this flaw in my implementation of the Enigma Machine, I have not encountered any instance where a character is output as itself in the running of this program.
