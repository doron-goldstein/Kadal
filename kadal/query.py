MEDIA_SEARCH = """
query ($search: String, $type: MediaType, $exclude: MediaFormat, $isAdult: Boolean) {
  Media(search: $search, type: $type, format_not: $exclude, isAdult: $isAdult) {
    id
    type
    format
    title {
      english
      romaji
      native
    }
    synonyms
    status
    description
    startDate {
      year
      month
      day
    }
    endDate {
      year
      month
      day
    }
    episodes
    chapters
    volumes
    coverImage {
      large
      color
    }
    bannerImage
    genres
    averageScore
    siteUrl
    nextAiringEpisode {
      timeUntilAiring
      episode
    }
  }
}
"""

MEDIA_BY_ID = """
query ($id: Int, $type: MediaType) {
  Media(id: $id, type: $type) {
    id
    type
    format
    title {
      english
      romaji
      native
    }
    synonyms
    status
    description
    startDate {
      year
      month
      day
    }
    endDate {
      year
      month
      day
    }
    episodes
    chapters
    coverImage {
      large
      color
    }
    bannerImage
    genres
    averageScore
    siteUrl
    nextAiringEpisode {
      timeUntilAiring
      episode
    }
  }
}
"""

MEDIA_PAGED = """
query (
  $id: Int,
  $page: Int,
  $perPage: Int,
  $search: String,
  $type: MediaType,
  $sort: [MediaSort] = [SEARCH_MATCH],
  $exclude: MediaFormat,
  $isAdult: Boolean
) {
  Page(page: $page, perPage: $perPage) {
    media(id: $id, search: $search, type: $type, sort: $sort, format_not: $exclude, isAdult: $isAdult) {
      id
      type
      format
      title {
        english
        romaji
        native
      }
      synonyms
      status
      description
      startDate {
        year
        month
        day
      }
      endDate {
        year
        month
        day
      }
      episodes
      chapters
      volumes
      coverImage {
        large
        color
      }
      bannerImage
      genres
      averageScore
      siteUrl
      popularity
    }
  }
}
"""

USER_SEARCH = """
query ($search: String) {
  User(search: $search) {
    id
    name
    html_about: about(asHtml: true)
    about
    avatar {
      large
    }
    bannerImage
    siteUrl
    stats {
      watchedTime
      chaptersRead
    }
  }
}
"""

USER_BY_ID = """
query ($id: Int) {
  User(id: $id) {
    id
    name
    html_about: about(asHtml: true)
    about
    avatar {
      large
    }
    bannerImage
    siteUrl
    stats {
      watchedTime
      chaptersRead
    }
  }
}
"""
