{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 155,
   "id": "9f6ce914",
   "metadata": {},
   "outputs": [],
   "source": [
    "employees1 = {\"name\": \"Ron Swanson\", \"age\": 55, \"department\": \"Management\", \"phone\": \"555-1234\", \"salary\": \",000\"}\n",
    "employees2 = {\"name\": \"Leslie Knope\", \"department\": \"Middle Management\", \"phone\": \"555-4321\"}\n",
    "employees3 = {\"name\": \"Andy Dwyer\", \"department\": \" Shoe Shining\", \"phone\": \"555-1122\"}\n",
    "employees4 = {\"name\": \"April Ludgate\", \"department\": \"Administration\", \"phone\": \"555-3345\"}\n",
    "             "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "id": "8008c170",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'Ron Swanson', 'age': 55, 'department': 'Management', 'phone': '555-1234', 'salary': ',000'} \n",
      " {'name': 'Leslie Knope', 'department': 'Middle Management', 'phone': '555-4321'} \n",
      " {'name': 'Andy Dwyer', 'department': ' Shoe Shining', 'phone': '555-1122'} \n",
      " {'name': 'April Ludgate', 'department': 'Administration', 'phone': '555-3345'}\n"
     ]
    }
   ],
   "source": [
    "print(employees1,\"\\n\", employees2,\"\\n\", employees3,\"\\n\", employees4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "id": "e494d51d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('name', 'Ron Swanson')\n",
      "('age', 55)\n",
      "('department', 'Management')\n",
      "('phone', '555-1234')\n",
      "('salary', ',000')\n"
     ]
    }
   ],
   "source": [
    "for key,values in employees1.items():\n",
    "    print((key,values))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "b1a2d25c",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'Ron Swanson', 'age': 55, 'department': 'Management', 'phone': '555-1234', 'salary': ',000'}\n",
      "{'name': 'Leslie Knope', 'department': 'Middle Management', 'phone': '555-4321'}\n",
      "{'name': 'Andy Dwyer', 'department': ' Shoe Shining', 'phone': '555-1122'}\n",
      "{'name': 'April Ludgate', 'department': 'Administration', 'phone': '555-3345'}\n"
     ]
    }
   ],
   "source": [
    "employees = [employees1, employees2, employees3, employees4]\n",
    "    \n",
    "for i in range(4):\n",
    "    print(employees[i])\n",
    "    #print(f\"{employees['name']} in {employees['department']} can be reached at {employees['phone']}\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "id": "39ed2609",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ron Swanson in Management can be reached at 555-1234\n"
     ]
    }
   ],
   "source": [
    " print(f\"{employees1['name']} in {employees1['department']} can be reached at {employees1['phone']}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1d978e1",
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
