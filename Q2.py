ciphertext = "DVNSJQRVPCGWBVZQGVVPVILQJVTURPBNPZNTGQIGSIGVWMTCIMFQUIACCKVGCBYKQZNTNBUCIENUHIVFIWPQCBNKCMIGGGVOEWEVPVGFXAPQKMEATDRTBIQGIPRNXJECGQNPLMYEDURFIPRXXAVVDZJKIPNUBQYGPVQGMXYCXVRFIPNVIPRIGMNVTAGVGMNUJZRKCBUGQCVNSQAILIFPDBNUXVTNTJBQZJHVIPRMCWJNTLTGIPNVRWAPTKGGSBUGBIYNTDRTNZBQBKBPIIVPTLZCCCFEGQCVHWAFXNSGGMAVHCOLTKGUXVPNJLVPVUNVWMZCIQPUPAGTDVBONXUKAWFQEPLOTLVEXVRGCOVPTMEKCONPSPVUIWEAIPRURPBNPZQGRQQGSBBUEMAFIPRFPGRZETBTXVTGKMEARWEPTZBHIPRNXJECGGGJTNVTHBEQDUPQCBNKCMQDDWXUDVZCIPROPBVEHBUGHKUQAIETTIQCQWHVCCZDTZFITWZGIZVEUQTWGMFCCLRNTONPIXEQDNFVWIGJPLVPHXVTTLTGCMECIQBPHWSVWQAMTZFQCMZCCCFEGQCVSMFEGQOGSPBYHQZRAMBDHMEXPBVQCAPQJTQNTIQVDLRGEBUGDZROHEUKAMNPDBUGGMKRAIVPTLUQLIOUIZNEIQQGPABHIMAHDCAFEZNEIQPCAICRAQPCIQBPHKRPICEKTAYCIMEVWMFEWWYCGZRCAQFGSBUCIUNVWMZCIQPULIFPDBZGGMYAPKBNAMPVXWAQUNBTBCYCHJHVPTNPVCNITNBTSMFEGQOKCOCCIBRTCANPSZRCHWAKCONDDCGVWMJQGTQ"

english_freq = [8.55, 1.60, 3.16, 3.87, 12.10, 2.18, 2.09, 4.96, 7.33, 0.22, 
                0.81, 4.21, 2.53, 7.17, 7.47, 2.07, 0.10, 6.33, 6.73, 8.94,
                2.68, 1.06, 1.83, 0.19, 1.72, 0.11]
#copy pasted cipher and requency for IoQ

#defining a helper to compute ioc for one string
def ioc(text):
    n = len(text)
    if n<2:
        return 0; #n<2 retunrs fasle to avoid a divide by zero case when the slide is too short
    counts = [0] *26

    for ch in text:
        index = ord(ch) - ord('A') #index as in Q1 without small letters
        counts[index] += 1

    numerator = 0
    for count in counts:
        numerator += count * (count-1) 

    #basically uisong the ioc formula given in the tutorial 
    denominator = n * n-1
    ic = 26 * numerator/denominator
    return ic
    #the  ioc calc return around 1.7 for english text and 1.0 for random text

#to estimate key length 
def est_key_len(cipher, max_len):
    best_len = 1
    best_diff = float('inf') #impossibly large difference

    for j in range(1,max_len + 1): #candidater key length defined by j, to take splices S1,S2 and so on 
        slices = []
        for start in range(j):
            slice_text = cipher[start::j]
            slices.append(slice_text)

        total_ic = 0 
        count =0 
        for s in slices: #compute ioc of each slice avg them and compare to 1.7 
            if len(s) >= 2:
                total_ic += ioc(s)
                count += 1

        if count == 0:
            continue

        avg_ic = total_ic / count #average ioc 
        diff = abs(avg_ic - 1.7)
        if diff<best_diff: #tracking best ioc i.e. closedst to 1.7 out of j = 1 to max_len
            best_diff = diff
            best_len = j

    return best_len 

