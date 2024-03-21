#include <string>
#include <vector>
#include <map>
#include <algorithm>

std::vector<int> solution(std::vector<std::string> id_list, std::vector<std::string> report, int k)
{
	std::vector<int> answer;
	std::map<std::string, int> reportList;

	for (int i = 0; i < id_list.size(); i++)  // id_list만큼 0 추가
	{
		answer.push_back(0);
	}

	std::sort(report.begin(), report.end());
	report.erase(std::unique(report.begin(), report.end()), report.end());  // 중복 원소 제거, 신고는 한 번만 인정

	//for (std::vector<std::string>::iterator i = report.begin(); i != report.end(); i++)
	for (int i = 0; i < report.size(); i++)
	{
		std::string temp;
		bool flag = false;

		for (int j = 0; j <= report[i].length(); j++)
		{
			if (flag)
			{
				temp += report[i][j];
			}

			if (report[i][j] == ' ')
			{
				flag = true;
			}
		}

		if (reportList[temp])
		{
			reportList[temp] += 1;
		}

		else
		{
			reportList[temp] = 1;
		}
	}

	for (auto i : reportList)
	{
		if (i.second >= k)  // 신고 기준치 초과시
		{
			for (int j = 0; j < report.size(); j++)  // report에서 신고자 추출
			{
				std::string temp;
				bool flag = false;

				for (int k = 0; k <= report[j].length(); k++)
				{
					if (flag)
					{
						temp += report[j][k];
					}

					if (report[j][k] == ' ')
					{
						flag = true;
					}
				}

				if (temp == i.first)  // 신고 당한 사람의 이름이 같다면
				{
					std::string reporter;

					for (int k = 0; k <= report[j].length(); k++)
					{
						if (report[j][k] == ' ')
						{
							break;
						}

						reporter += report[j][k];
					}

					for (int k = 0; k < id_list.size(); k++)
					{
						if (id_list[k] == reporter)
						{
							answer[k] += 1;
						}
					}
				}
			}
		}
	}

	return answer;
}
