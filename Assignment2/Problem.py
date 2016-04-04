from numpy import *

class Problem:
    attributes=[]
    user1=[]
    user2=[]
    user1profile=[]
    user2profile=[]
    matrix=zeros((20,10))
    numattr=[]
    IDF=[]

    def getAttributes(self,line):
        for cell in line:
            if cell=="":
                return
            self.attributes.append(cell)
        return
    def loadLine(self,index,line):
        if index==-1:
            self.getAttributes(line[1:11])
        elif index<20:
            colum=-1
            for cell in line:
                if cell.isdigit() and colum<10:
                    self.matrix[index,colum]=float(cell)
                colum+=1
                if colum==14:
                    if cell=='':
                        self.user1.append(0.0)
                    else:
                        self.user1.append(float(cell))
                if colum==15:
                    if cell=='':
                        self.user2.append(0.0)
                    else:
                        self.user2.append(float(cell))

    def computeProfile(self):
        userlp1=zeros(shape(self.matrix))
        userlp2=zeros(shape(self.matrix))
        for j in range(10):
            userlp1[:,j]=self.matrix[:,j]*self.user1
            userlp2[:,j]=self.matrix[:,j]*self.user2
        self.user1profile=sum(userlp1,axis=0)
        self.user2profile=sum(userlp2,axis=0)
        print "Compute user1profile"
        print self.user1profile
        print "Compute user2 profile"
        print self.user2profile

    def predictuser1(self):
        for i in range(20):
            # if self.user1[i]!=0:
            #     continue
            self.user1[i]=sum(self.matrix[i,:]*self.user1profile)
        print "user1 prediction:"
        print self.user1

    def predictuser2(self):
        for i in range(20):
            if self.user2[i]!=0:
                continue
            self.user2[i]=sum(self.matrix[i,:]*self.user2profile)
        print "user2 prediction:"
        print self.user2

    def normalize(self):
        self.numattr=sum(self.matrix,axis=1)
        print self.numattr
        for row in range(20):
            s=self.matrix[row,:]/sqrt(self.numattr[row])
            self.matrix[row,:]=s
        print "Normalized matrix:"
        print self.matrix

    def computeDF(self):
        self.IDF=1/sum(self.matrix,axis=0)
        self.normalize()
        self.computeProfile()
        for doc in range(20):
            self.user1[doc]=sum(self.matrix[doc,:]*self.user1profile*self.IDF,axis=0)
            self.user2[doc]=sum(self.matrix[doc,:]*self.user2profile*self.IDF,axis=0)
        print self.user1
        print self.user2