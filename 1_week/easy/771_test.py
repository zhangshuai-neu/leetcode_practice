J = "aA";
S = "aAAbbbb";
count = 0;
j_len = len(J);
s_len = len(S);

#建一个词典
stone_type_dict = {};

for i in range(j_len):
	stone_type_dict[J[i]]=0;

for i in range(s_len):
	if S[i] in stone_type_dict:
		stone_type_dict[S[i]] = stone_type_dict[S[i]] + 1
		
for i in range(j_len):
	count = stone_type_dict[J[i]] + count;
	
print(count);
		
		
