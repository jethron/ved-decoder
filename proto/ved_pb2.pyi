from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ved(_message.Message):
    __slots__ = ["link_index", "link_type", "mysterious_msg", "result_position", "start_result_position", "sub_result_position", "v10", "v11", "v12", "v15", "v3", "v4", "v8", "v9"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class M15(_message.Message):
        __slots__ = ["v1", "v2"]
        V1_FIELD_NUMBER: _ClassVar[int]
        V2_FIELD_NUMBER: _ClassVar[int]
        v1: int
        v2: int
        def __init__(self, v1: _Optional[int] = ..., v2: _Optional[int] = ...) -> None: ...
    class Mysterious(_message.Message):
        __slots__ = ["nested_mysterious_msg"]
        class NestedMysterious(_message.Message):
            __slots__ = ["mysterious1", "mysterious2", "ts"]
            MYSTERIOUS1_FIELD_NUMBER: _ClassVar[int]
            MYSTERIOUS2_FIELD_NUMBER: _ClassVar[int]
            TS_FIELD_NUMBER: _ClassVar[int]
            mysterious1: int
            mysterious2: int
            ts: int
            def __init__(self, ts: _Optional[int] = ..., mysterious1: _Optional[int] = ..., mysterious2: _Optional[int] = ...) -> None: ...
        NESTED_MYSTERIOUS_MSG_FIELD_NUMBER: _ClassVar[int]
        nested_mysterious_msg: Ved.Mysterious.NestedMysterious
        def __init__(self, nested_mysterious_msg: _Optional[_Union[Ved.Mysterious.NestedMysterious, _Mapping]] = ...) -> None: ...
    Jump_to_link: Ved.Type
    LINK_INDEX_FIELD_NUMBER: _ClassVar[int]
    LINK_TYPE_FIELD_NUMBER: _ClassVar[int]
    MYSTERIOUS_MSG_FIELD_NUMBER: _ClassVar[int]
    RESULT_POSITION_FIELD_NUMBER: _ClassVar[int]
    START_RESULT_POSITION_FIELD_NUMBER: _ClassVar[int]
    SUB_RESULT_POSITION_FIELD_NUMBER: _ClassVar[int]
    V10_FIELD_NUMBER: _ClassVar[int]
    V11_FIELD_NUMBER: _ClassVar[int]
    V12_FIELD_NUMBER: _ClassVar[int]
    V15_FIELD_NUMBER: _ClassVar[int]
    V3_FIELD_NUMBER: _ClassVar[int]
    V4_FIELD_NUMBER: _ClassVar[int]
    V8_FIELD_NUMBER: _ClassVar[int]
    V9_FIELD_NUMBER: _ClassVar[int]
    adword_oneline_sitelink: Ved.Type
    adword_sitelink: Ved.Type
    authorship_by_author_link: Ved.Type
    authorship_thumbnail_link: Ved.Type
    blog_search_result: Ved.Type
    book_search_result_author_link: Ved.Type
    breadcrumb: Ved.Type
    dictionary_definition_link: Ved.Type
    image_search_result: Ved.Type
    image_search_result_in_basic_image_search_universal_search: Ved.Type
    image_search_result_preview_View_image_link: Ved.Type
    image_search_result_preview_Visit_page_link: Ved.Type
    image_search_result_preview_grey_website_link_underneath_title: Ved.Type
    image_search_result_preview_thumbnail: Ved.Type
    image_search_result_preview_title_link: Ved.Type
    image_search_result_thumbnail: Ved.Type
    indepth_article_result: Ved.Type
    indepth_article_result_thumbnail: Ved.Type
    knowledge_graph_link: Ved.Type
    knowledge_graph_main_image: Ved.Type
    knowledge_graph_repeated_sub_link: Ved.Type
    link_index: int
    link_type: Ved.Type
    local_search_result: Ved.Type
    local_search_result_marker_pin_icon: Ved.Type
    map_search_result: Ved.Type
    map_search_result_thumbnail: Ved.Type
    map_search_result_website_link: Ved.Type
    more_results_link_listed_mainly_for_QA_websites: Ved.Type
    mysterious_msg: Ved.Mysterious
    new_image_search_result: Ved.Type
    news_result: Ved.Type
    news_result_thumbnail: Ved.Type
    news_result_video_thumbnail: Ved.Type
    news_sub_result: Ved.Type
    normal_result_thumbnail_1: Ved.Type
    normal_result_thumbnail_2: Ved.Type
    normal_universal_search_result: Ved.Type
    oneline_sitelink: Ved.Type
    patent_result: Ved.Type
    patent_result_Overview_Related_Discuss_link: Ved.Type
    patent_result_thumbnail: Ved.Type
    result_position: int
    shopping_search_result: Ved.Type
    sitelink: Ved.Type
    sponsored_search_result: Ved.Type
    sponsored_shopping_result: Ved.Type
    sponsored_shopping_result_main_column_of_universal_search: Ved.Type
    sponsored_shopping_result_thumbnail: Ved.Type
    sponsored_shopping_result_thumbnail_2: Ved.Type
    start_result_position: int
    sub_result_position: int
    v10: int
    v11: int
    v12: int
    v15: Ved.M15
    v3: int
    v4: int
    v8: int
    v9: int
    video_result: Ved.Type
    video_result_thumbnail: Ved.Type
    def __init__(self, link_index: _Optional[int] = ..., link_type: _Optional[_Union[Ved.Type, str]] = ..., sub_result_position: _Optional[int] = ..., result_position: _Optional[int] = ..., start_result_position: _Optional[int] = ..., v3: _Optional[int] = ..., v4: _Optional[int] = ..., v8: _Optional[int] = ..., v9: _Optional[int] = ..., v10: _Optional[int] = ..., v11: _Optional[int] = ..., v12: _Optional[int] = ..., mysterious_msg: _Optional[_Union[Ved.Mysterious, _Mapping]] = ..., v15: _Optional[_Union[Ved.M15, _Mapping]] = ...) -> None: ...
