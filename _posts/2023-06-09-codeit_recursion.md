{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def triangle_number(n):\n",
    "    if n == 1:\n",
    "        return 1\n",
    "    else:\n",
    "        return n + triangle_number(n-1)\n",
    "\n",
    "triangle_number(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "triangle_number(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n",
      "6\n",
      "10\n",
      "15\n",
      "21\n",
      "28\n",
      "36\n",
      "45\n",
      "55\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 11):\n",
    "    print(triangle_number(i))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def fib(n):\n",
    "    if n == 1 or n == 2:\n",
    "        return 1\n",
    "    else:\n",
    "        return fib(n-1) + fib(n-2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "8\n",
      "13\n",
      "21\n",
      "34\n",
      "55\n",
      "89\n",
      "144\n",
      "233\n",
      "377\n",
      "610\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 16):\n",
    "    print(fib(i))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def sum_digits(n):\n",
    "    if n < 10:\n",
    "        return n\n",
    "    else:\n",
    "        return sum_digits(n//10) + sum_digits(n%10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "14"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum_digits(22541)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "14"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n = 22541\n",
    "s = 0\n",
    "for i in range(len(str(n))):\n",
    "    k = int(str(n)[i])\n",
    "    s += k\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def max_list(my_list):\n",
    "    if len(my_list) == 1:\n",
    "        return my_list[0]\n",
    "    else:\n",
    "        return max_list(my_list[:len(my_list)-1])     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[18], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m elist \u001b[39m=\u001b[39m [\u001b[39m1\u001b[39m, \u001b[39m4\u001b[39m, \u001b[39m3\u001b[39m, \u001b[39m2\u001b[39m, \u001b[39m5\u001b[39m, \u001b[39m0\u001b[39m, \u001b[39m2\u001b[39m]\n\u001b[1;32m----> 2\u001b[0m elist[\u001b[39m7\u001b[39;49m]\n",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "elist = [1, 4, 3, 2, 5, 0, 2]\n",
    "elist[len(elist)-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "def max_list(my_list):\n",
    "    if len(my_list) == 1:\n",
    "        return my_list[0]\n",
    "    if max_list(my_list[:len(my_list)-1]) < my_list[len(my_list)-1]:\n",
    "        return my_list[len(my_list)-1]\n",
    "    else:\n",
    "        return max_list(my_list[:len(my_list)-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.8\n"
     ]
    }
   ],
   "source": [
    "print(max_list([1, 2.7, -3, 2.8, 1.6]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_palindrome(my_str):\n",
    "    if len(my_str) <= 1:\n",
    "        return True\n",
    "    elif my_str[0] == my_str[-1]:\n",
    "        return is_palindrome(my_str[1:len(my_str)-1])\n",
    "    else:\n",
    "        return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "print(is_palindrome('121'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "False\n",
      "True\n",
      "True\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "print(is_palindrome('기러기'))\n",
    "print(is_palindrome('토마토'))\n",
    "print(is_palindrome('바나나'))\n",
    "print(is_palindrome('racecar'))\n",
    "print(is_palindrome('radar'))\n",
    "print(is_palindrome('stars'))\n",
    "print(is_palindrome('123321'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_palindrome(my_str):\n",
    "    # 베이스 케이스\n",
    "    if len(my_str) <= 1:\n",
    "        return True\n",
    "\n",
    "    # 재귀 케이스\n",
    "    if my_str[0] != my_str[-1]:\n",
    "        return False \n",
    "\n",
    "    return is_palindrome(my_str[1: -1])\n",
    "#반복하는 케이스를 반환값으로 두었다. 이게 보기에 더 낫다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "False\n",
      "True\n",
      "True\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "print(is_palindrome('기러기'))\n",
    "print(is_palindrome('토마토'))\n",
    "print(is_palindrome('바나나'))\n",
    "print(is_palindrome('racecar'))\n",
    "print(is_palindrome('radar'))\n",
    "print(is_palindrome('stars'))\n",
    "print(is_palindrome('123321'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def power(x, n):\n",
    "    if n == 0:\n",
    "        return 1\n",
    "    elif n == 1:\n",
    "        return x\n",
    "    elif n % 2 == 0:\n",
    "        return power(x, n//2) * power(x, n//2)\n",
    "    else:\n",
    "        return power(x, n//2) * power(x, n//2) *  x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10 % 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n",
      "1\n",
      "1419857\n",
      "129140163\n",
      "68719476736\n"
     ]
    }
   ],
   "source": [
    "print(power(2, 3))\n",
    "print(power(5, 0))\n",
    "print(power(17, 5))\n",
    "print(power(3, 17))\n",
    "print(power(4, 18))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "def flip(some_list):\n",
    "    if len(some_list) == 1:\n",
    "        return some_list\n",
    "    else:\n",
    "        return some_list[-1:] + flip(some_list[:-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 8, 7, 6, 5, 4, 3, 2, 1]"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]\n",
    "flip(some_list)\n",
    "# print(some_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6, 7, 8]"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(some_list)\n",
    "some_list[:len(some_list)-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def move_disk(disk_num, start_peg, end_peg):\n",
    "    print(\"%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동\" % (disk_num, start_peg, end_peg))\n",
    "\n",
    "\n",
    "def hanoi(num_disks, start_peg, end_peg):\n",
    "    other_peg = 6 - end_peg - start_peg    \n",
    "    if num_disks == 0:\n",
    "        return\n",
    "    # elif num_disks == 1:\n",
    "    #     return move_disk(1, 1, 3)\n",
    "    # elif num_disks >= 2:\n",
    "    #     return hanoi(2, 1, 3)\n",
    "    else:\n",
    "        move_disk(num_disks, start_peg, end_peg)\n",
    "        return hanoi(num_disks - 1, start_peg, other_peg)"
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
      "3번 원판을 1번 기둥에서 3번 기둥으로 이동\n",
      "2번 원판을 1번 기둥에서 2번 기둥으로 이동\n",
      "1번 원판을 1번 기둥에서 3번 기둥으로 이동\n"
     ]
    }
   ],
   "source": [
    "hanoi(3, 1, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "[1se]\n",
    "1se\n",
    "\n",
    "[2se]\n",
    "1so\n",
    "2se\n",
    "1oe\n",
    "\n",
    "*3se\n",
    "2so\n",
    "1se\n",
    "2oe\n",
    "\n",
    "*4se\n",
    "3so\n",
    "1se\n",
    "3eo\n",
    "\n",
    "*513\n",
    "412\n",
    "113\n",
    "423"
   ]
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
   "version": "3.10.11"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
