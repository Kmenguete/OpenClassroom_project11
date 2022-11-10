from gudlft.main import create_club, create_competition


class ClubMockResponse:

    @staticmethod
    def get_info():
        return {"name": "club_test",
                "email": "example@gmail.com",
                "points": "30"}


class CompetitionMockResponse:

    @staticmethod
    def get_info():
        return {"name": "Competition Test",
                "date": "2022-06-09 10:00:00",
                "numberOfPlaces": "50"}


def test_create_club(mocker):
    mocker.patch('main.Club', return_value=ClubMockResponse())
    expected_value = {"name": "club_test",
                      "email": "example@gmail.com",
                      "points": "30"}
    assert create_club() == expected_value


def test_create_competition(mocker):
    mocker.patch('main.Competition', return_value=CompetitionMockResponse())
    expected_value = {"name": "Competition Test",
                      "date": "2022-06-09 10:00:00",
                      "numberOfPlaces": "50"}
    assert create_competition() == expected_value
