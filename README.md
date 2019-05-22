{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><H1>PYTHON $ - JSON Dictionaty</H1>\n",
    "<h2> few examples of how to do that with fJSON Files.</h2><h3>Let us load a GeoJSON file representing the data dictionary.\n",
    "In[ut a specific word to search and print the results.</h3></p>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    " uses Json file as data dictionary\n",
    " searches and shows the information found\n",
    " '''\n",
    "\n",
    "\n",
    "from difflib import get_close_matches\n",
    "import json\n",
    "\n",
    "def print_lines(data_collectionm):\n",
    "    #print(type(data_collectionm))\n",
    "    if type(data_collectionm)==list:\n",
    "        for lin in data_collectionm:\n",
    "            print(\" - \" + lin)\n",
    "    else:\n",
    "        print(data_collectionm)\n",
    "\n",
    "def get_jsonInfo(word,data):\n",
    "    if word in data:\n",
    "        return (data[word])\n",
    "    elif w.title() in data: #if user entered \"texas\" this will check for \"Texas\" as well.\n",
    "        return data[w.title()]\n",
    "    elif w.upper() in data: #in case user enters words like USA or NATO\n",
    "        return data[w.upper()]\n",
    "    elif len(get_close_matches(word.lower(),data.keys())) > 0:\n",
    "        yn=input(\"Do you mean %s instead? Enter (y=Yesm n=No)?\" % get_close_matches(word.lower(),data.keys())[0])\n",
    "        if yn=='y':\n",
    "            return (data[get_close_matches(word.lower(),data.keys())[0]])\n",
    "        elif yn=='n':\n",
    "            return (\"word '%s' does'nt exist!. Please double check it.\" % word)\n",
    "        else:\n",
    "            return (\"I did not understand your Entry.\")\n",
    "    else:\n",
    "        return (\"word '%s' not foud!. Please double check it.\" % word)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('data.json',\"r\") as json_data:\n",
    "    source=json_data.read()\n",
    "data = json.loads(source)\n",
    "#data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter word? train\n",
      " - A self-propelled, connected group of vehicles moving on rails.\n",
      " - To point or cause to go (blows, weapons, or objects such as photographic equipment) towards\n",
      " - To develop behaviour by instruction and practice.\n",
      " - A group of animals, vehicles, or people that follow one another in a line.\n",
      " - To do physical exercise to improve one's fitness.\n",
      " - To exercise in order to prepare for an event or competition.\n",
      " - To teach by training.\n",
      " - To undergo training or instruction for a particular role, function, or profession.\n",
      " - To educate for a future role or function.\n",
      " - To act as a trainer or coach (to), as in sports.\n"
     ]
    }
   ],
   "source": [
    "word = input(\"Enter word? \")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print_lines(get_jsonInfo(word,data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
