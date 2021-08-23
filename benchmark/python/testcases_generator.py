pattern = \
    "\n    def test_{}(self):\n" + \
    "        test_update({})"

file = open('gen.txt', 'w')
for i in range(1, 200):
    file.write(pattern.format(i, i))
file.close()