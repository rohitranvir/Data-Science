{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "44dc0ef9-5632-473c-9a2c-2f3b19f9b1f4",
   "metadata": {},
   "source": [
    "## Arithmetic operator on string  \" + ,* ,In ,Not in ,< , <= ,>= , == , != \""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9c7be8d9-980e-4431-8c77-28b105b853a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RohitRanvir\n",
      "Rohit10\n"
     ]
    }
   ],
   "source": [
    "s1=\"Rohit\"\n",
    "s2=\"Ranvir\"\n",
    "s3=10\n",
    "print(s1+s2)\n",
    "print(s1+str(s3))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6cb87020-3013-4112-a283-2fd3ba96e016",
   "metadata": {},
   "source": [
    "## WE can multiply string with int but no with string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "47890340-7636-4e33-b2c7-20acde4d8392",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "abab\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "can't multiply sequence by non-int of type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[7]\u001b[39m\u001b[32m, line 5\u001b[39m\n\u001b[32m      3\u001b[39m i3=\u001b[33m\"\u001b[39m\u001b[33mcd\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m      4\u001b[39m \u001b[38;5;28mprint\u001b[39m(i1*s)\n\u001b[32m----> \u001b[39m\u001b[32m5\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[43mi3\u001b[49m\u001b[43m*\u001b[49m\u001b[43ms\u001b[49m)\n",
      "\u001b[31mTypeError\u001b[39m: can't multiply sequence by non-int of type 'str'"
     ]
    }
   ],
   "source": [
    "s=\"ab\"\n",
    "i1=2\n",
    "i3=\"cd\"\n",
    "print(i1*s)\n",
    "# print(i3*s)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03c8be1d-a442-4c29-837a-da69721767fd",
   "metadata": {},
   "source": [
    "## member ship operator  \" in \" and \"not in\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a8d597f9-52ee-4d4f-b161-d01d744b932c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "s=\"Rohit\"\n",
    "s1=\"Ro\"\n",
    "print('b' in s)\n",
    "print(s1 in s)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c73f328c-57db-44d6-81f7-2542755e577a",
   "metadata": {},
   "source": [
    "## comparesion operator \" Compare ascii Value\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "fbe4f1ca-23aa-4a35-bda1-9acf00cd183d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "print(\"ABC\"< \"XYZ\")\n",
    "print(\"abc\"<\"XYZ\")\n",
    "print(\"ABC\"<=\"ABC\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e4cc717e-3601-4e95-8bb0-74fc1c15226c",
   "metadata": {},
   "source": [
    "## Commaon function "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "82df6dc0-9d51-48c1-9954-055549238e83",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "t\n",
      "h\n",
      "['h', 'i', 'o', 'r', 't']\n",
      "['t', 'r', 'o', 'i', 'h']\n",
      "114\n",
      "a\n",
      "A\n"
     ]
    }
   ],
   "source": [
    "s=\"rohit\"\n",
    "print(len(s))\n",
    "print(max(s))\n",
    "print(min(s))\n",
    "print(sorted(s))\n",
    "print(sorted(s,reverse=True))\n",
    "print(ord('r'))\n",
    "print(chr(97))\n",
    "print(chr(65))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1117a763-90ad-4f4d-b5f5-903a823f6ffb",
   "metadata": {},
   "source": [
    "## String specific method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "95c935c3-e760-4ece-8df7-658cd4cf646e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "welcome  to data science\n",
      "WELCOME  TO DATA SCIENCE\n",
      "wELCOME  tO dATA SCIENCE\n",
      "Welcome  to data science\n",
      "Welcome  To Data Science\n"
     ]
    }
   ],
   "source": [
    "s=\"Welcome  To Data science\"\n",
    "print(s.lower())\n",
    "print(s.upper())\n",
    "print(s.swapcase())\n",
    "print(s.capitalize())\n",
    "print(s.title())2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d97042e-3ad4-42f1-9022-fbecdf82807b",
   "metadata": {},
   "source": [
    "## Count(substr) ==>                                                                                                                                                  it return number of occurance of given substring"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "33f57315-e9d7-4f9e-80e2-1ac6a969c808",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "s=\"abababaabaabbafdfsj\"\n",
    "print(s.count('a'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5db216af-1c4c-47db-a6cf-692c93be225d",
   "metadata": {},
   "source": [
    "## Replace(old,new)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "89d73651-37cf-4582-a5a4-807a03f86108",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bbbcbbc\n"
     ]
    }
   ],
   "source": [
    "s=\"abacbac\"\n",
    "print(s.replace('a','b'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9f73feee-6315-4c93-8328-4afdec37cf4d",
   "metadata": {},
   "source": [
    "## Endswith( )   ==>  it return true if the given string ends with another string else false "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "20eb3d62-d9b4-459c-9c37-fde0fdc67493",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "s=\"Python is very easy\"\n",
    "print(s.endswith(\"easy\"))\n",
    "print(s.endswith(\"rohit\"))\n",
    "\n",
    "\n",
    "\n",
    "print(s.startswith(\"Python\"))\n",
    "print(s.startswith(\"python\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "34e6abce-e83d-4d15-931c-958955a12ba3",
   "metadata": {},
   "source": [
    "## index(Substring)    =>    it return a index of substring in the main string else error\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "76d2952a-0907-4120-b26b-25f94af0ddb3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "substring not found",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mValueError\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[48]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[32m      1\u001b[39m s=\u001b[33m\"\u001b[39m\u001b[33mpython is very easy\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m      2\u001b[39m \u001b[38;5;28mprint\u001b[39m(s.index(\u001b[33m\"\u001b[39m\u001b[33mis\u001b[39m\u001b[33m\"\u001b[39m))\n\u001b[32m----> \u001b[39m\u001b[32m3\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[43ms\u001b[49m\u001b[43m.\u001b[49m\u001b[43mindex\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mwas\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m)\n",
      "\u001b[31mValueError\u001b[39m: substring not found"
     ]
    }
   ],
   "source": [
    "s=\"python is very easy\"\n",
    "print(s.index(\"is\"))\n",
    "print(s.index(\"was\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0d17d117-0045-4d4d-a6fb-e85ec3ea3190",
   "metadata": {},
   "source": [
    "## find(Substring) => it return a index of substring in the main string else return -1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "faf49e09-ff1f-4cc3-921c-9407802e54f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "-1\n"
     ]
    }
   ],
   "source": [
    "s=\"python is very easy\"\n",
    "print(s.find(\"is\"))\n",
    "print(s.find(\"was\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cb4d7f21-4f58-47bc-9154-b27cce2f994f",
   "metadata": {},
   "source": [
    "## split(delimetr) => it split the string base on delimeter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "de9bc34d-177f-40da-8f68-10452454ece6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['python', 'is', 'very', 'easy']\n",
      "['1', '02', '2005']\n"
     ]
    }
   ],
   "source": [
    "s=\"python is very easy\"\n",
    "print(s.split(\" \"))\n",
    "s1='1/02/2005'\n",
    "print(s1.split(\"/\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "55657b59-7916-49b7-ad32-0cf72ca39957",
   "metadata": {},
   "source": [
    "## seperator.join(list)     =>    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "a74f03be-d5c3-4de2-bc74-e632fcdd6651",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python is very easy\n",
      "python/is/very/easy\n",
      "python:is:very:easy\n"
     ]
    }
   ],
   "source": [
    "l=[\"python\",\"is\",\"very\",\"easy\"]\n",
    "print(\" \".join(l))\n",
    "print(\"/\".join(l))\n",
    "print(\":\".join(l))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb419713-66e9-45b0-a41b-34ff92265b66",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
