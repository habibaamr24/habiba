{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNf3RpWH1Kauak3+OuIo0vD",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/habibaamr24/habiba/blob/main/untitled2.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "yvkWtWt-zzZa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "eGqtPj9ZLz1G"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "BNboI62_WYrI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Kb7-Jhe-yW-M",
        "outputId": "1d42b796-4588-4594-89f4-0999f714ab09"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello user welcome to my game \n",
            "You will start with 50 points\n",
            "Youre score is currently\n",
            "50\n",
            "I will give you some options to choose from\n",
            "every right choice you get some points and every wrong choice you lose some points \n",
            "let's start\n",
            "You woke up and found yourself on a planet in the dark space\n",
            "You tried screaming for help but no one was there with you\n",
            "You turned back and suddenly you saw an alien\n"
          ]
        }
      ],
      "source": [
        "def play_the_game():#this function is responsable for running the code\n",
        "  import time\n",
        "  import random\n",
        "  import sys\n",
        "  def hello_function():\n",
        "    print(\"Hello user welcome to my game \")\n",
        "    time.sleep(2)# this function delays printing the next statment as it stimulate real life storytelling\n",
        "  hello_function()\n",
        "  def explination_function():\n",
        "    score=50\n",
        "    print(\"You will start with 50 points\")\n",
        "    time.sleep(2)\n",
        "    print(\"Youre score is currently\")\n",
        "    print(score)\n",
        "    print(\"I will give you some options to choose from\")\n",
        "    time.sleep(2)\n",
        "    print(\"every right choice you get some points and every wrong choice you lose some points \")\n",
        "    time.sleep(2)\n",
        "    print(\"let's start\")\n",
        "    time.sleep(2)\n",
        "    print(\"You woke up and found yourself on a planet in the dark space\")\n",
        "    time.sleep(2)\n",
        "    print(\"You tried screaming for help but no one was there with you\")\n",
        "    time.sleep(2)\n",
        "    print(\"You turned back and suddenly you saw an alien\")\n",
        "  explination_function()\n",
        "  while True:\n",
        "    response = input(\"Should you ATTACK the Alien or RUN AWAY (ATTACK OR RUN AWAY)\")\n",
        "    if response.upper() == \"ATTACK\":# I used this function to make the input uppercase so it canbe more intense and give suspense to the user\n",
        "      print(\"Your score is now\")\n",
        "      time.sleep(2)\n",
        "      score = score +20\n",
        "      print(score)\n",
        "      print(\" good job you killed the alien you are not in danger anymore\")\n",
        "      break\n",
        "    elif response.uper() == \"RUN AWAY\":\n",
        "        print(\"Your score is now\")\n",
        "        score = score -20\n",
        "        print(score)\n",
        "        print(\"It's okay you found a place to hide and the alien walked away\")\n",
        "        break\n",
        "\n",
        "  else:\n",
        "        print(\"Invalid response. Please enter 'ATTACK' or 'RUN AWAY'.\")\n",
        "  print(\"an evile astronaut came and wanted to fight you\")\n",
        "  time.sleep(2)\n",
        "  print(\"And now it's time to choose a weapon\")\n",
        "  time.sleep(2)\n",
        "  print(\"The weapon you choose will effect your points\")\n",
        "  while True:\n",
        "    response = input(\"Would you rather have a gun or a bow (gun or bow)\").lower()# this function makes all letters that is given by the user lowercase\n",
        "    if response == \"gun\":\n",
        "      print(\"Your score is now\")\n",
        "      time.sleep(2)\n",
        "      score = score -10\n",
        "      print(score)\n",
        "      print(\"you missed and you got injured but he left you alone he just wanted to explore the planet\")\n",
        "      time.sleep(2)\n",
        "      break\n",
        "    elif response == \"bow\":\n",
        "      print(\"Your score is now\")\n",
        "      score = score +10\n",
        "      print(score)\n",
        "      print(\"you defeated the evile astronaut\")\n",
        "      break\n",
        "\n",
        "    else:\n",
        "     print(\"Invalid response. Please enter 'gun' or 'bow'.\")\n",
        "  def motivation_function():\n",
        "     print(\"Good Job! So proud of you that you made it this far\")\n",
        "     time.sleep(2)\n",
        "  motivation_function()\n",
        "  print(\"It's now youre last option wether you win or lose\")\n",
        "  while True:\n",
        "        response = input(\"You are now given the option wether to teleport to another planet or stay on this one (other planet or same planet)\")\n",
        "        if response.lower() == \"same planet\":\n",
        "          print(\"Your score is now\")\n",
        "          time.sleep(2)\n",
        "          score = score -20\n",
        "          print(score)\n",
        "          print(\" no one came to help you \")\n",
        "          time.sleep(2)\n",
        "          break\n",
        "        elif response.lower() == \"other planet\":\n",
        "          print(\"Your score is now\")\n",
        "          score = score +20\n",
        "          print(score)\n",
        "          list1 = [ \"mercury\", \"jupiter\", \"venus\"]\n",
        "          print(\"You are now on\")\n",
        "          print(random.choice(list1))\n",
        "          print(\"a bunch of astronaut came and helped you return to earth\")\n",
        "          print(\"Good choice\")\n",
        "          break\n",
        "        else:\n",
        "          print(\"Invalid response. Please enter 'other planet' or 'same planet'.\")\n",
        "  while True:\n",
        "    if score == 100 :\n",
        "      print(\"Great Job ! You won :)\")\n",
        "      break\n",
        "    else:\n",
        "      print(\"Better luck next time :()\")\n",
        "      break\n",
        "  while True:\n",
        "    restart=input(\"Do you want to play again(yes or no)\").lower()\n",
        "    if restart == \"yes\":\n",
        "      play_the_game()# this function helps run the code when the user wnats to resatre the game\n",
        "      break\n",
        "    elif restart == \"no\":\n",
        "      print(\"Goodbye! Hope you enjoyed my game\")\n",
        "      exit\n",
        "      break\n",
        "    else:\n",
        "         print(\"Invalid response. Please enter 'yes' or 'no'.\")\n",
        "play_the_game()\n"
      ]
    }
  ]
}
