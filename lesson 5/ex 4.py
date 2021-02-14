with open('numbers.txt', 'r') as donor:
    with open('rnumbers.txt', 'w') as acceptor:
        acceptor.write(donor.readline().replace('One', 'Один')+'\n')
        acceptor.write(donor.readline().replace('Two', 'Два')+'\n')
        acceptor.write(donor.readline().replace('Three', 'Три')+'\n')
        acceptor.write(donor.readline().replace('Four', 'Четыре')+'\n')
