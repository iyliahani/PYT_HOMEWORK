{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c426e73d",
   "metadata": {},
   "outputs": [],
   "source": [
    "class BankAccount:\n",
    "    balance = 0\n",
    "    \n",
    "    def __init__(self, accountType=\"Savings\"):\n",
    "        self.accountType = accountType\n",
    "        accountType = \"Savings\"\n",
    "        \n",
    "    def deposit(self, balance):\n",
    "        amount = input(\"Enter amount to be deposited: \")\n",
    "        self.balance += amount\n",
    "        print(\"\\n Amount Deposited:\", amount)\n",
    "        \n",
    "    def withdraw(self, balance):\n",
    "        amount = input(\"Enter amount to be withdrawn: \")\n",
    "        if self.balance >= amount:\n",
    "            self.balance -= amount\n",
    "            print(\"\\n You Withdrew:\", amount)\n",
    "        else:\n",
    "            print(\"\\n Insufficient balance  \")\n",
    "            \n",
    "    def display(self):\n",
    "        print(\"\\n Net Available Balance=\",self.balance)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "62ef6b1b",
   "metadata": {},
   "outputs": [],
   "source": [
    "s = BankAccount()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8afcb37e",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "deposit() missing 1 required positional argument: 'balance'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [4]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43ms\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdeposit\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[1;31mTypeError\u001b[0m: deposit() missing 1 required positional argument: 'balance'"
     ]
    }
   ],
   "source": [
    "s.deposit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a4fe2b8",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
