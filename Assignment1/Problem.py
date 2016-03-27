class Problem:
    ratings=[]
    movienames=[]

    def loadline(self,line):
        position=0
        for cell in line:
            if position!=0:
                if cell!="" and not cell.isdigit():
                    self.ratings.append([])
                    self.movienames.append(cell)
                elif cell.isdigit():
                    self.ratings[position-1].append(int(cell))
                else:
                    self.ratings[position-1].append(-1)
            position=position+1

    def meanRatings(self):
        result=[]
        for ratings in self.ratings:
            num=0.0
            average=0.0
            for star in ratings:
                if star!=-1:
                    num=num+1
                    average=average+star
            result.append(float(average/num))
        return result

    def mostRatings(self):
        result=[]
        for ratings in self.ratings:
            num=0
            for star in ratings:
                if star!=-1:
                    num=num+1
            result.append(num)
        return result

    def rating4(self):
        result=[]
        for ratings in self.ratings:
            num=0.0
            sum=0.0
            for star in ratings:
                if star!=-1 and star>3:
                    num=num+1
                if star!=-1:#notice!
                    sum=sum+1
            result.append(float(num/sum))
        return result
    def getXY(self):
        num=0.0
        nums=[]
        for i in range(1,len(self.ratings)):
            num=0.0
            for j in range(0,len(self.ratings[0])):
                if self.ratings[0][j]!=-1 and self.ratings[i][j]!=-1:
                    num=num+1
            nums.append(num)
        return nums
    def getRelevance(self):
        nums=self.getXY()
        num=0.0
        for star in self.ratings[0]:
           if star!=-1:
               num=num+1
        nums=[float(i/num) for i in nums]
        return nums