def solution(N):
        gaps = []
        binary = bin(N)[2:]

        have_one = False
        gap = 0
        for i in range(len(binary)):
            if binary[i] == '1' and not have_one:
                have_one = True

            elif binary[i] == '1' and have_one:
                gaps.append(gap)
                gap = 0

            elif binary[i] == '0' and have_one:
                gap += 1

        return 0 if len(gaps) == 0 else max(gaps)
solution(529)


