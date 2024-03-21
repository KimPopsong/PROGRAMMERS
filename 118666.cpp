#include <string>
#include <vector>

using namespace std;

string solution(vector<string> survey, vector<int> choices)
{
	string answer = "";
	int RT = 0, CF = 0, JM = 0, AN = 0;

	std::vector<int>::iterator iterChoices = choices.begin();
	for (std::vector<std::string>::iterator iterSurvey = survey.begin(); iterSurvey != survey.end(); iterSurvey++, iterChoices++)
	{
		if (*iterSurvey == "RT")
		{
			RT += *iterChoices - 4;
		}

		else if (*iterSurvey == "TR")
		{
			RT += (*iterChoices - 4) * -1;
		}

		else if (*iterSurvey == "CF")
		{
			CF += *iterChoices - 4;
		}

		else if (*iterSurvey == "FC")
		{
			CF += (*iterChoices - 4) * -1;
		}

		else if (*iterSurvey == "JM")
		{
			JM += *iterChoices - 4;
		}

		else if (*iterSurvey == "MJ")
		{
			JM += (*iterChoices - 4) * -1;
		}

		else if (*iterSurvey == "AN")
		{
			AN += *iterChoices - 4;
		}

		else if (*iterSurvey == "NA")
		{
			AN += (*iterChoices - 4) * -1;
		}
	}

	if (RT <= 0)
	{
		answer += "R";
	}

	else
	{
		answer += "T";
	}

	if (CF <= 0)
	{
		answer += "C";
	}

	else
	{
		answer += "F";
	}

	if (JM <= 0)
	{
		answer += "J";
	}

	else
	{
		answer += "M";
	}

	if (AN <= 0)
	{
		answer += "A";
	}

	else
	{
		answer += "N";
	}

	return answer;
}
