#include <string>
#include <vector>
#include <map>
#include <sstream>

std::vector<int> solution(std::vector<int> fees, std::vector<std::string> records)
{
	std::vector<int> answer;
	std::map<std::string, int> calcTime;  // 차량번호, 주차시간
	std::map<std::string, bool> checkInOut; // 차량번호, 출차여부

	for (int i = 0; i < records.size(); i++)
	{
		std::vector<std::string> temp;  // 문자열 분리
		std::istringstream stringSplit(records[i]);
		std::string stringBuffer;
		while (std::getline(stringSplit, stringBuffer, ' '))
		{
			temp.push_back(stringBuffer);
		}

		int time = (temp[0][0] - '0') * 600 + (temp[0][1] - '0') * 60 + (temp[0][3] - '0') * 10 + (temp[0][4] - '0');  // 분으로 환산하여 저장

		if (temp[2] == "IN")  // IN 일시 입차 시간을 빼고
		{
			if (calcTime.count(temp[1]))  // 이미 입차 출차했다면
			{
				calcTime[temp[1]] -= time;
			}

			else  // 처음 입차라면
			{
				calcTime[temp[1]] = -1 * time;
			}

			checkInOut[temp[1]] = true;  // In 확인
		}

		else if (temp[2] == "OUT")  // OUT 일시 입차 시간을 더함
		{
			calcTime[temp[1]] += time;

			checkInOut[temp[1]] = false;  // Out 확인
		}
	}

	for (auto i : checkInOut)  // In 하고 Out 하지 않은 차 확인
	{
		if (i.second)
		{
			calcTime[i.first] += 1439;
		}
	}

	for (auto i : calcTime)  // 주차 요금 계산
	{
		int fee = 0;

		if (i.second <= fees[0])
		{
			fee += fees[1];
		}

		else
		{
			i.second -= fees[0];
			fee += fees[1];

			fee += i.second / fees[2] * fees[3];

			if (i.second % fees[2] != 0)
			{
				fee += fees[3];
			}
		}

		answer.push_back(fee);
	}

	return answer;
}

int main()
{
	std::vector<int> fees = { 180, 5000, 10, 600 };
	std::vector<std::string> records = { "05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT" };

	solution(fees, records);

	return 0;
}
