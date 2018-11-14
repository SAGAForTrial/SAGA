import numpy as np
np.set_printoptions(threshold=np.nan)

with open(r'./result.csv') as file:
    cache = ''
    x= ''
    N = 0
    Nlist = []
    lines = file.readlines();
    for ii,line in enumerate(lines):
        if line == "\n":
            del lines[ii]
    for line in lines:
        words = line.split(',')
        x =  ','.join(words[4:])[:-1]
        if x != cache:
            Nlist.append(N)
        cache = ','.join(words[:4])
        N+=1

lineAddBlank = lines[:]
with open(r'../result_blank','w+') as file:
    for x in Nlist[::-1]:
        lineAddBlank.insert(x,'\n')
    file.writelines(lineAddBlank)

list = []
x = np.array(Nlist[1:])
y = np.array(Nlist[:-1])
z =x -y

print(z.max())
print(x[z.argmax(axis=0)],":",y[z.argmax(axis=0)])







with open(r'./result_final.csv','w') as file:
    cache = len(lines)
    cloneClasses = []
    for x in Nlist[::-1]:
        cloneClassText = lines[x:cache]
        cloneClass = []
        for y in cloneClassText:
            words = y.split(',')
            cloneClass.append(','.join(words[4:])[:-1])
        cloneClass.append(','.join(words[:4]))
        cloneClasses.append(cloneClass)
        cache = x


    for cloneClass in cloneClasses:
        for idx,x in enumerate(cloneClass[:-1]):
            for y in cloneClass[idx+1:]:
                #file.write('1,'+ x + ',' + y + '\n')
                file.write(x + ',' + y + '\n')
              #  file.write(y + ',' + x + '\n')



tonum = 0
for cloneClass in cloneClasses:
    x = len(cloneClass)
    tonum += x*(x-1)/2


print(tonum)




'''
SELECT count(*) 
FROM
(
(
(
SELECT X.type as type1, X.name as name1, X.startline as startline1, X.endline as endline1, Y.type as type2, Y.name as name2, Y.startline as startline2, Y.endline as endline2
FROM
(
SELECT *
FROM clones
WHERE syntactic_type = 1
)  as clean_clones, functions as X, functions as Y
WHERE clean_clones.function_id_one = X."id" AND clean_clones.function_id_two = Y."id"
) 
UNION
(
SELECT X.type as type1, X.name as name1, X.startline as startline1, X.endline as endline1, Y.type as type2, Y.name as name2, Y.startline as startline2, Y.endline as endline2
FROM
(
SELECT *
FROM clones
WHERE syntactic_type = 1
) as clean_clones, functions as X, functions as Y
WHERE clean_clones.function_id_one = Y."id" AND clean_clones.function_id_two = X."id"
)  
) 
INTERSECT
(
SELECT type1, name1,  startline1, endline1, type2, name2, startline2, endline2
FROM "tools_clones"
)
) as R


'''