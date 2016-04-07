from numpy import *
class Problem:
    users=[]
    movies=[]
    matrix=zeros((100,25))
    cor=zeros((25,25),dtype=object)
    nearneibor=zeros((25,5),dtype=object)
    def loadline(self,line,index):
        if index==0:
            for cell in line:
                if cell!="":
                    self.users.append(cell)
        else:
            col=0
            for cell in line:
                 if col==0:
                     self.movies.append(cell)
                 elif cell!="":
                     self.matrix[index-1,col-1]=float(cell)
                 else:
                     self.matrix[index-1,col-1]=-1.0
                 col+=1


    def computecorelation(self):
        for user1 in range(25):
            for user2 in range(25):
                #self.cor[user1,user2]=round(self.pearson_def(self.matrix[:,user1],self.matrix[:,user2]),6)
                self.cor[user1,user2]=round(self.calcuUserCorraltions(self.matrix[:,user1],self.matrix[:,user2]),6)
        print self.cor
    def average_def(self,x):
        valid=0.0
        sum=0.0
        for i in x:
            if i!=-1:
                sum+=i
                valid+=1
        return float(sum)/float(valid)
    #don't know why it is wrong
    def pearson_def(self,x, y):
        n = len(x)
        avg_x = self.average_def(x)
        avg_y = self.average_def(y)
        diffprod = 0.0
        xdiff2 = 0.0
        ydiff2 = 0.0
        for idx in range(n):
            if x[idx]!=-1 and y[idx]!=-1:
                xdiff = x[idx] - avg_x
                ydiff = y[idx] - avg_y
                diffprod += (xdiff *ydiff)
                xdiff2 +=math.pow(xdiff,2)
                ydiff2 += math.pow(ydiff,2)
        return diffprod/math.sqrt(xdiff2* ydiff2)
    #correct version
    def calcuUserCorraltions(self,user1,user2):
        assert len(user1)==len(user2)
        validUser1Data=[]
        validUser2Data=[]
        for u1,u2 in zip(user1,user2):
            if u1!=-1 and u2!=-1:
                validUser1Data.append(u1)
                validUser2Data.append(u2)
        statisticProfile1=self.calcuStandDeviation(validUser1Data)
        statisticProfile2=self.calcuStandDeviation(validUser2Data)
        numerator=0
        for u1,u2 in zip(validUser1Data,validUser2Data):
            numerator+=(u1-statisticProfile1[1])*(u2-statisticProfile2[1])
        correlation=numerator/(statisticProfile1[0]*statisticProfile2[0])
        return  correlation
    def calcuMean(self,data):
        sum=0
        for d in data:
            sum+=d
        return sum/float(len(data))
    def calcuStandDeviation(self,data):
        mean=self.calcuMean(data)
        deviation=0
        for d in data:
            deviation+=math.pow(d-mean,2)
        return [math.sqrt(deviation),mean]

    def calcuNearneibor(self):
        for index in range(25):
            indexs=argsort(-self.cor[index,:])
            for iindex in range(5):
                self.nearneibor[index,iindex]=indexs[iindex+1] # exclude the target user
        print self.nearneibor

    def predict(self,user):
        #noseefilms=[]
        movieindex=0

        # for movies in self.matrix[:,user]:
        #     if movies==-1:
        #         noseefilms.append(movieindex)
        #     movieindex+=1
        predictvalues={}
        for movies in range(100):
            prediction=0
            sumweights=0
            for coruser in self.nearneibor[user]:
                if self.matrix[movies,coruser]==-1:
                    continue
                prediction+=self.matrix[movies,coruser]*self.cor[user,coruser]
                sumweights+=self.cor[user,coruser]
            if sumweights==0:
                predictvalues[self.movies[movies]]=0
            else:
                predictvalues[self.movies[movies]]=prediction/sumweights
        predictvalues=sorted(predictvalues.iteritems(),key=lambda d:d[1],reverse=True)
        print predictvalues
    def predictnormalized(self,user):
        predictvalues={}
        avgmatrix=zeros((25,1))
        for i in range(25):
            avgmatrix[i,0]=self.average_def(self.matrix[:,i])
        for movies in range(100):
            prediction=0
            sumweights=0
            for coruser in self.nearneibor[user]:
                if self.matrix[movies,coruser]==-1:
                    continue
                prediction+=(self.matrix[movies,coruser]-avgmatrix[coruser,0])*self.cor[user,coruser]
                sumweights+=self.cor[user,coruser]
            if sumweights==0:
                predictvalues[self.movies[movies]]=avgmatrix[user,0]
            else:
                predictvalues[self.movies[movies]]=prediction/sumweights+avgmatrix[user,0]
        predictvalues=sorted(predictvalues.iteritems(),key=lambda d:d[1],reverse=True)
        print predictvalues