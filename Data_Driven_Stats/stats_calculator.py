def mean(data):
    return sum(data) / len(data)

def median(data):
      data.sort()
      n = len(data)
      if n % 2 == 0:
         return (data[n//2-1] + data[n//2]) / 2
      else:
         return data[n//2]

def mode(data):
      return max(data, key=data.count)

def variance(data):
      mean = sum(data) / len(data)
      return sum((x - mean) ** 2 for x in data) / len(data)

def std_dev(data):
      return variance(data) ** 0.5

def sample_variance(data):
      mean = sum(data) / len(data)
      return sum((x - mean) ** 2 for x in data) / (len(data) - 1)

def stats_summary(data):
      return {
         'mean': mean(data),
         'median': median(data),
         'mode': mode(data),
         'variance': variance(data),
         'std_dev': std_dev(data),
         'sample_variance': sample_variance(data)
      }

def main():
   will_continue = True
   
   while will_continue:
      data = input("Enter the data separated by spaces: ")
      data = list(map(float, data.split(','))) 
      print(stats_summary(data))
      
      will_continue = input("Do you want to continue? (yes/no): ").lower() == 'yes'

if __name__ == "__main__":
   main()